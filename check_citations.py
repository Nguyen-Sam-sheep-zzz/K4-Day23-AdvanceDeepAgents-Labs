"""check_citations.py - STUDENT IMPLEMENTS `check`.   Runs INSIDE the sandbox (standard library only).

research.py uploads this file to the sandbox and the lead agent runs it with the `execute` tool:
    python3 /tmp/work/research/check_citations.py [report.md] [sources.json]
It must exit 0 and print "OK: ..." when the report is consistent, else print each problem and exit 1.
"""
import json
import re
import sys
from urllib.parse import urlsplit

REPORT = "/tmp/work/report/report.md"
SOURCES = "/tmp/work/research/sources.json"


def _blank(text):
    """Mask ignored Markdown while preserving line positions."""
    return "".join("\n" if char == "\n" else " " for char in text)


def _without_code(text):
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            lines.append(_blank(line))
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker and (marker[1][0] != "`" or "`" not in marker[2]):
            fence = marker[1]
            lines.append(_blank(line))
        else:
            lines.append(line)
    text = "".join(lines)
    runs = list(re.finditer(r"`+", text))
    chunks, start, i = [], 0, 0
    while i < len(runs):
        opening = runs[i]
        if _escaped(text, opening.start()):
            i += 1
            continue
        closing = next((j for j in range(i + 1, len(runs)) if len(runs[j][0]) == len(opening[0])), None)
        if closing is None:
            i += 1
            continue
        end = runs[closing].end()
        chunks.extend((text[start:opening.start()], _blank(text[opening.start():end])))
        start, i = end, closing + 1
    chunks.append(text[start:])
    return "".join(chunks)


def _escaped(text, index):
    slashes = 0
    while index > 0 and text[index - 1] == "\\":
        index -= 1
        slashes += 1
    return slashes % 2 == 1


def _balanced_end(text, start, opening, closing):
    depth = 0
    for i in range(start, len(text)):
        if _escaped(text, i):
            continue
        if text[i] == opening:
            depth += 1
        elif text[i] == closing:
            depth -= 1
            if depth == 0:
                return i + 1
    return None


def _without_links(text):
    definitions = set()
    pattern = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[^\n]*", re.MULTILINE)
    for match in pattern.finditer(text):
        definitions.add(" ".join(match[1].lower().split()))
    text = pattern.sub(lambda match: _blank(match[0]), text)
    chunks, start, i = [], 0, 0
    while i < len(text):
        if text[i] != "[" or _escaped(text, i):
            i += 1
            continue
        label_end = _balanced_end(text, i, "[", "]")
        if label_end is None:
            i += 1
            continue
        label = " ".join(text[i + 1:label_end - 1].lower().split())
        end = None
        if text[label_end:label_end + 1] == "(":
            end = _balanced_end(text, label_end, "(", ")")
        elif text[label_end:label_end + 1] == "[":
            ref_end = _balanced_end(text, label_end, "[", "]")
            if ref_end:
                reference = " ".join(text[label_end + 1:ref_end - 1].lower().split()) or label
                if reference in definitions:
                    end = ref_end
        elif label in definitions:
            end = label_end
        if end:
            chunks.extend((text[start:i], _blank(text[i:end])))
            start, i = end, end
        else:
            i += 1
    chunks.append(text[start:])
    return "".join(chunks)


def _valid_url(url):
    if not isinstance(url, str) or not url.startswith(("http://", "https://")) or re.search(r"\s", url):
        return False
    try:
        parsed = urlsplit(url)
        return bool(parsed.hostname) and parsed.port != 0
    except ValueError:
        return False


def _reference_urls(line, expected):
    urls = []
    for match in re.finditer(r"https?://[^\s<>`\"']+", line):
        url = match[0]
        if url != expected:
            # Markdown delimiters are not part of the destination. Preserve
            # balanced parentheses that actually belong to an URL path.
            while url.endswith(")") and url.count(")") > url.count("("):
                url = url[:-1]
            while url.endswith("]") and url.count("]") > url.count("["):
                url = url[:-1]
            if url != expected:
                url = url.rstrip(".,;")
        urls.append(url)
    return urls


def check(report_text, sources):
    """Validate source/citation/reference consistency without modifying inputs.

    This structural check cannot determine whether a cited claim is true.
    Numeric groups and ascending ranges are accepted; each range is bounded
    to 10,000 members to prevent accidental unbounded expansion.
    """
    problems = []
    if not isinstance(sources, list):
        return ["sources.json must be a JSON array of source objects"]
    if not sources:
        return ["no sources in sources.json"]
    numbers, urls = {}, set()
    for index, source in enumerate(sources, 1):
        if not isinstance(source, dict):
            problems.append(f"source entry {index} must be an object")
            continue
        n, url = source.get("n"), source.get("url")
        valid_n = type(n) is int and n > 0
        if not valid_n:
            problems.append(f"source entry {index}: n must be a positive integer")
        elif n in numbers:
            problems.append(f"duplicate n [{n}] in sources.json")
        else:
            numbers[n] = url
        if not _valid_url(url):
            problems.append(f"source entry {index}: url must be a valid http(s) URL")
        elif url in urls:
            problems.append(f"source entry {index}: duplicate url in sources.json")
        else:
            urls.add(url)
    if not isinstance(report_text, str):
        return problems + ["report must be text"]
    visible = _without_code(report_text)
    headings = list(re.finditer(r"^ {0,3}##[ \t]+References[ \t]*(?:#+[ \t]*)?\r?$", visible, re.MULTILINE))
    if not headings:
        return problems + ["missing ## References heading"]
    if len(headings) != 1:
        problems.append("References must occur exactly once as the final section")
    heading = headings[0]
    body = _without_links(visible[:heading.start()])
    cited = set()
    for match in re.finditer(r"\[([0-9\s,\-–]+)\]", body):
        if _escaped(body, match.start()):
            continue
        expression = match[1]
        try:
            for part in expression.split(","):
                bounds = re.fullmatch(r"\s*([0-9]{1,100})(?:\s*[-–]\s*([0-9]{1,100}))?\s*", part)
                if not bounds:
                    raise ValueError
                first = int(bounds[1])
                last = int(bounds[2]) if bounds[2] else first
                if first <= 0 or last < first or last - first >= 10000:
                    raise ValueError
                cited.update(range(first, last + 1))
        except ValueError:
            problems.append("invalid or excessively large numeric citation")
    for n in sorted(cited - numbers.keys()):
        problems.append(f"[{n}] cited but missing from sources.json")
    for n in sorted(numbers.keys() - cited):
        problems.append(f"source [{n}] never cited")
    counts = {}
    for line in report_text[heading.end():].splitlines():
        if not line.strip():
            continue
        entry = re.match(r"^\[([0-9]{1,100})\](?:[ \t]+|$)", line)
        if not entry:
            problems.append("References must be the final section and contain only [n] reference lines")
            continue
        n = int(entry[1])
        counts[n] = counts.get(n, 0) + 1
        if n not in numbers:
            problems.append(f"reference [{n}] missing from sources.json")
        found_urls = _reference_urls(line, numbers.get(n))
        if len(found_urls) != 1:
            problems.append(f"reference [{n}] must contain exactly one URL (found {len(found_urls)})")
        elif n in numbers and found_urls[0] != numbers[n]:
            problems.append(f"reference [{n}] url does not match sources.json")
    for n in sorted(numbers):
        if counts.get(n, 0) != 1:
            problems.append(f"source [{n}] needs exactly one reference line (found {counts.get(n, 0)})")
    for n in sorted(counts.keys() - numbers.keys()):
        if counts[n] > 1:
            problems.append(f"duplicate reference [{n}]")
    return problems


def main(argv):
    report_path = argv[1] if len(argv) > 1 else REPORT
    sources_path = argv[2] if len(argv) > 2 else SOURCES
    try:
        with open(report_path, encoding="utf-8") as f:
            report = f.read()
        with open(sources_path, encoding="utf-8") as f:
            sources = json.load(f)
    except (OSError, ValueError) as exc:
        print(f"cannot read inputs: {exc}")
        return 1
    problems = check(report, sources)
    if problems:
        print("\n".join(problems))
        return 1
    print(f"OK: {len(sources)} sources, all citations resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
