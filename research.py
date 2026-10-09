"""Run sandboxed deep research and publish only validated survey artifacts."""
import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import time
import unicodedata
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import AIMessage, ToolMessage

from agents import FINALIZER_PATH, REPORT_PATH, SOURCES_PATH, VALIDATOR_PATH, WORKDIR, build_lead_agent
from check_citations import check
from model import make_model
from sandbox import download, open_sandbox, upload
from tools import _redact

ROOT = Path(__file__).parent
REPORTS = ROOT / "reports"
VALIDATOR_SOURCE = ROOT / "check_citations.py"
FINALIZER_SOURCE = ROOT / "finalize_citations.py"
SOURCE_TAGS = {"arxiv", "hf-daily", "hf-search", "web"}
REQUIRED_HEADINGS = ("TL;DR", "Background", "Trends and open problems", "References")


class ToolProgress(BaseCallbackHandler):
    """Show tool progress without logging arguments or fetched content."""

    def on_tool_start(self, serialized, input_str, **kwargs):
        name = str((serialized or {}).get("name") or "tool")
        safe_name = re.sub(r"[^A-Za-z0-9_-]", "", name)[:50] or "tool"
        print(f"[research] tool: {safe_name}", flush=True)


def slugify(topic):
    """Return a bounded, Windows-safe ASCII filename stem for untrusted input."""
    normalized = unicodedata.normalize("NFKD", str(topic or ""))
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")[:60].rstrip("-") or "topic"
    reserved = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
    return f"topic-{slug}" if slug.upper() in reserved else slug


def build_prompt(topic, review_feedback=""):
    """Give the lead a real local date and the required output boundaries."""
    today = datetime.now(timezone(timedelta(hours=7))).date().isoformat()
    prompt = (
        f"Research topic: {topic.strip()}\n"
        f"Current date in Asia/Saigon: {today}. Treat this as the current date; "
        "do not assume sources newer than the date exist. Cover relevant foundations and "
        "the last two years where the evidence permits, and state source dates accurately.\n"
        "Produce an English survey with 3-6 substantive thematic sections in the required "
        "report template. Mandatory headings are literal and case-sensitive: ## TL;DR, "
        "## Background, ## Trends and open problems, ## References. Do not title-case "
        "the Trends and open problems heading. After finalization, verify every named method "
        "and number against the actual matching source record and its notes; do not cite "
        "one paper as evidence for a different named paper. Use only retrieved, attributable sources, keep the source tag equal "
        "to the actual retrieval tool, and ensure at least three distinct source tags survive "
        "finalization. Complete all delegation, citation checking, finalization and validation "
        "steps in the system instructions. Report evidence gaps honestly."
    )
    if review_feedback and str(review_feedback).strip():
        safe_feedback = re.sub(r"[\x00-\x1f\x7f]+", " ", _redact(str(review_feedback))).strip()[:4000]
        prompt += ("\nReviewer feedback for this run (verify against retrieved sources and correct "
                   "the report where warranted): " + safe_feedback)
    return prompt


def parse_cli(argv):
    """Parse optional review feedback without losing unquoted topic words."""
    parser = argparse.ArgumentParser(description="Run deep research on a topic")
    parser.add_argument("topic", nargs="*")
    parser.add_argument("--review-feedback", default="", help="Specific reviewer findings to verify during research")
    args = parser.parse_args(argv)
    return " ".join(args.topic), args.review_feedback


def _message_field(message, name, default=None):
    return message.get(name, default) if isinstance(message, dict) else getattr(message, name, default)


def summarize(messages, elapsed, model_name):
    """Count lead requests and match successful task results by tool call ID."""
    tool_calls = Counter()
    tokens = {"input": 0, "output": 0}
    researcher_calls = checker_calls = max_parallel_researchers = 0
    task_roles = {}
    successful_results = set()
    for message in messages:
        if isinstance(message, ToolMessage) or _message_field(message, "type") == "tool":
            call_id = _message_field(message, "tool_call_id")
            status = _message_field(message, "status", "success")
            content = _message_field(message, "content", "")
            if (isinstance(call_id, str) and call_id and status == "success"
                    and not (isinstance(content, str) and content.lstrip().lower().startswith("error:"))):
                successful_results.add(call_id)
            continue
        if not (isinstance(message, AIMessage) or _message_field(message, "type") == "ai"):
            continue
        parallel_researchers = 0
        for call in _message_field(message, "tool_calls", []) or []:
            if not isinstance(call, dict):
                continue
            name = call.get("name")
            if not isinstance(name, str) or not name:
                continue
            tool_calls[name] += 1
            if name == "task":
                args = call.get("args")
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except ValueError:
                        args = {}
                role = args.get("subagent_type") if isinstance(args, dict) else None
                call_id = call.get("id")
                if role in ("researcher", "citation-checker") and isinstance(call_id, str) and call_id:
                    task_roles.setdefault(call_id, role)
                if role == "researcher":
                    researcher_calls += 1
                    parallel_researchers += 1
                elif role == "citation-checker":
                    checker_calls += 1
        max_parallel_researchers = max(max_parallel_researchers, parallel_researchers)
        usage = _message_field(message, "usage_metadata") or {}
        if isinstance(usage, dict):
            for name, field in (("input", "input_tokens"), ("output", "output_tokens")):
                value = usage.get(field)
                if type(value) is int and value >= 0:
                    tokens[name] += value
    return {"model": model_name, "elapsed_s": round(elapsed, 1),
            "subagent_calls": tool_calls["task"], "tool_calls": dict(tool_calls),
            "tokens": tokens, "researcher_calls": researcher_calls,
            "checker_calls": checker_calls, "max_parallel_researchers": max_parallel_researchers,
            "successful_researcher_calls": sum(task_roles.get(call_id) == "researcher" for call_id in successful_results),
            "successful_checker_calls": sum(task_roles.get(call_id) == "citation-checker" for call_id in successful_results),
            "token_scope": "lead_messages_only"}


class OutputValidationError(RuntimeError):
    """Downloaded report or metadata failed a recoverable output gate."""


def _validated_sources(raw):
    if not isinstance(raw, bytes) or not raw:
        raise OutputValidationError("sources.json is missing or empty")
    try:
        sources = json.loads(raw.decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise OutputValidationError("sources.json is not valid UTF-8 JSON") from exc
    if not isinstance(sources, list) or not sources:
        raise OutputValidationError("sources.json must be a nonempty array")
    tags = set()
    for number, source in enumerate(sources, 1):
        if not isinstance(source, dict) or any(key not in source for key in ("n", "id", "url", "title", "date", "source")):
            raise OutputValidationError(f"source {number} is missing required fields")
        if type(source["n"]) is not int or source["n"] != number:
            raise OutputValidationError(f"source {number} has nonsequential numbering")
        if any(not isinstance(source[key], str) for key in ("id", "url", "title", "date", "source")):
            raise OutputValidationError(f"source {number} has an invalid field type")
        if not all(source[key].strip() for key in ("id", "url", "title")):
            raise OutputValidationError(f"source {number} has an empty id, url or title")
        tag, url, source_id = source["source"], source["url"], source["id"]
        if tag not in SOURCE_TAGS:
            raise OutputValidationError(f"source {number} has an unknown retrieval tag")
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname or any(c.isspace() for c in url):
            raise OutputValidationError(f"source {number} has an invalid URL")
        if tag == "arxiv" and url != f"https://arxiv.org/abs/{source_id}":
            raise OutputValidationError(f"source {number} has a mismatched arxiv id or URL")
        if tag in ("hf-daily", "hf-search") and url != f"https://huggingface.co/papers/{source_id}":
            raise OutputValidationError(f"source {number} has a mismatched Hugging Face id or URL")
        tags.add(tag)
    if len(tags) < 3:
        raise OutputValidationError("fewer than three source tags survived finalization")
    return sources, sorted(tags)


def _validated_report(raw, sources):
    if not isinstance(raw, bytes) or not raw:
        raise OutputValidationError("report.md is missing or empty")
    try:
        report = raw.decode("utf-8")
    except UnicodeError as exc:
        raise OutputValidationError("report.md is not UTF-8") from exc
    if not report.strip() or not re.search(r"^# .+", report, re.MULTILINE):
        raise OutputValidationError("report.md has no survey title")
    section_matches = list(re.finditer(r"^##[ \t]+([^\r\n]+?)[ \t]*\r?$", report, re.MULTILINE))
    headings = [match.group(1) for match in section_matches]
    if any(headings.count(heading) != 1 for heading in REQUIRED_HEADINGS):
        raise OutputValidationError("report.md lacks required sections")
    if not (headings[0:2] == ["TL;DR", "Background"] and headings[-2:] == ["Trends and open problems", "References"]):
        raise OutputValidationError("report.md sections are out of order")
    if not 3 <= len(headings[2:-2]) <= 6:
        raise OutputValidationError("report.md needs 3-6 thematic sections")
    sections = {headings[index]: report[match.end():section_matches[index + 1].start() if index + 1 < len(section_matches) else len(report)]
                for index, match in enumerate(section_matches)}
    for heading in headings[:-1]:
        if not sections[heading].strip():
            raise OutputValidationError(f"report.md has an empty {heading} section")
    bullets = re.findall(r"^[ \t]*[-*+][ \t]+\S[^\r\n]*", sections["TL;DR"], re.MULTILINE)
    if not 3 <= len(bullets) <= 5 or any(not re.search(r"(?<!\\)\[\d+(?:\s*(?:,|[-–])\s*\d+)*\](?!\s*\()", bullet) for bullet in bullets):
        raise OutputValidationError("TL;DR needs 3-5 cited Markdown bullets")
    problems = check(report, sources)
    if problems:
        raise OutputValidationError("citation validation failed: " + "; ".join(problems[:3]))


def _publish_trio(files):
    """Stage every byte first, then replace with rollback of any previous trio."""
    root = next(iter(files)).parent
    root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".research-stage-", dir=root) as directory:
        stage = Path(directory)
        staged = {}
        backups = {}
        for index, (destination, content) in enumerate(files.items()):
            pending = stage / f"new-{index}"
            pending.write_bytes(content)
            staged[destination] = pending
            if destination.exists():
                backup = stage / f"old-{index}"
                shutil.copy2(destination, backup)
                backups[destination] = backup
        replaced = []
        try:
            for destination, pending in staged.items():
                os.replace(pending, destination)
                replaced.append(destination)
        except OSError:
            for destination in reversed(replaced):
                if destination in backups:
                    os.replace(backups[destination], destination)
                else:
                    destination.unlink(missing_ok=True)
            raise


def save_outputs(backend, topic, messages, elapsed, model_name, reports_dir=REPORTS):
    """Validate downloaded originals, then publish report, sources and true metadata."""
    files = download(backend, [REPORT_PATH, SOURCES_PATH])
    report_bytes, sources_bytes = files.get(REPORT_PATH), files.get(SOURCES_PATH)
    sources, families = _validated_sources(sources_bytes)
    _validated_report(report_bytes, sources)
    metadata = {"topic": topic, **summarize(messages, elapsed, model_name),
                "n_sources": len(sources), "source_families": families}
    if metadata["subagent_calls"] < 3:
        raise OutputValidationError("fewer than three observed task calls")
    if metadata["researcher_calls"] < 3 or metadata["max_parallel_researchers"] < 3:
        raise OutputValidationError("no observed batch of at least three parallel researcher tasks")
    if metadata["checker_calls"] < 1:
        raise OutputValidationError("no observed citation-checker task")
    if metadata["successful_researcher_calls"] < 3:
        raise OutputValidationError("fewer than three successful researcher task results")
    if metadata["successful_checker_calls"] < 1:
        raise OutputValidationError("no successful citation-checker task result")
    slug = slugify(topic)
    reports_dir = Path(reports_dir)
    report_path = reports_dir / f"{slug}.md"
    artifacts = {report_path: report_bytes,
                 reports_dir / f"{slug}.sources.json": sources_bytes,
                 reports_dir / f"{slug}.meta.json": (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode("utf-8")}
    _publish_trio(artifacts)
    return report_path


def _require_command(backend, command, label, *, require_ok=False):
    result = backend.execute(command)
    if result.exit_code != 0 or (require_ok and not str(result.output).lstrip().startswith("OK:")):
        raise RuntimeError(f"{label} failed: {_redact(str(result.output)[:300])}")


def main(topic, review_feedback=""):
    """Return 0 on validated output, 1 on failure, 2 for an empty topic."""
    if not topic or not topic.strip():
        print("Usage: python research.py <topic>", file=sys.stderr)
        return 2
    try:
        print("[research] configuring model and sandbox", flush=True)
        model = make_model()
        model_name = getattr(model, "model_name", None) or getattr(model, "model", None) or os.getenv("LAB_MODEL", "unknown")
        started = time.monotonic()
        with open_sandbox() as backend:
            print("[research] preparing sandbox", flush=True)
            _require_command(backend, f"mkdir -p {WORKDIR}/research/notes {WORKDIR}/report", "sandbox setup")
            upload(backend, {VALIDATOR_PATH: VALIDATOR_SOURCE.read_bytes(),
                             FINALIZER_PATH: FINALIZER_SOURCE.read_bytes()})
            _require_command(backend, f"test -s {VALIDATOR_PATH} && test -s {FINALIZER_PATH}", "script upload")
            agent = build_lead_agent(backend, model)
            print("[research] running agent", flush=True)
            result = agent.invoke({"messages": [{"role": "user", "content": build_prompt(topic, review_feedback)}]},
                                  config={"recursion_limit": 1000, "callbacks": [ToolProgress()]})
            if not isinstance(result, dict) or not isinstance(result.get("messages"), list):
                raise RuntimeError("agent returned no message history")
            for repair_attempt in range(2):
                print("[research] finalizing and validating citations", flush=True)
                _require_command(backend, f"python3 {FINALIZER_PATH}", "citation finalizer")
                _require_command(backend, f"python3 {VALIDATOR_PATH}", "citation validator", require_ok=True)
                try:
                    path = save_outputs(backend, topic, result["messages"], time.monotonic() - started,
                                        str(model_name), REPORTS)
                    break
                except OutputValidationError as exc:
                    if repair_attempt:
                        raise
                    diagnostic = re.sub(r"[\r\n\t]+", " ", _redact(str(exc)))[:400]
                    feedback = (
                        "The output gate rejected the current sandbox report: " + diagnostic + ". "
                        "Treat this as a diagnostic, then repair report.md and sources.json in the sandbox. "
                        "Match each named method to its cited source and verify source IDs and URLs. "
                        "Run the citation-checker again, then finish the report. "
                        "This is the only repair attempt."
                    )
                    print("[research] requesting one sandbox output repair", flush=True)
                    result = agent.invoke({"messages": [*result["messages"], {"role": "user", "content": feedback}]},
                                          config={"recursion_limit": 1000, "callbacks": [ToolProgress()]})
                    if not isinstance(result, dict) or not isinstance(result.get("messages"), list):
                        raise RuntimeError("agent returned no message history after repair")
        print(f"[research] saved {path}", flush=True)
        return 0
    except Exception as exc:
        print(f"FAILED: {_redact(type(exc).__name__ + ': ' + str(exc))}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(*parse_cli(sys.argv[1:])))
