"""Offline tests for the research runner and its file publication boundary."""

import json
import os
import tempfile
import unittest
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

import research


def fixture():
    sources = [
        {"n": 1, "id": "2501.00001", "url": "https://arxiv.org/abs/2501.00001", "title": "Paper A", "date": "2025-01-01", "source": "arxiv"},
        {"n": 2, "id": "2501.00002", "url": "https://huggingface.co/papers/2501.00002", "title": "Paper B", "date": "2025-01-02", "source": "hf-search"},
        {"n": 3, "id": "https://example.org/c", "url": "https://example.org/c", "title": "Page C", "date": "", "source": "web"},
    ]
    report = ("# Survey\n\n## TL;DR\n- Finding A [1].\n- Finding B [2].\n- Finding C [3].\n\n## Background\nContext [1].\n\n"
              "## Methods\nComparison [1][2].\n\n## Evaluation\nResults [2][3].\n\n"
              "## Limitations\nGaps [3].\n\n## Trends and open problems\nTrend [1][3].\n\n"
              "## References\n[1] Paper A. arxiv. https://arxiv.org/abs/2501.00001 (2025-01-01)\n"
              "[2] Paper B. hf-search. https://huggingface.co/papers/2501.00002 (2025-01-02)\n"
              "[3] Page C. web. https://example.org/c ()\n").encode()
    return report, json.dumps(sources, ensure_ascii=False, indent=2).encode()


def messages():
    return [HumanMessage(content="research"), AIMessage(content="", tool_calls=[
        {"name": "task", "args": {"subagent_type": "researcher", "description": "A"}, "id": "1"},
        {"name": "task", "args": {"subagent_type": "researcher", "description": "B"}, "id": "2"},
        {"name": "task", "args": {"subagent_type": "researcher", "description": "C"}, "id": "3"},
        {"name": "write_todos", "args": {}, "id": "4"},
    ], usage_metadata={"input_tokens": 10, "output_tokens": 5, "total_tokens": 15}),
        AIMessage(content="", tool_calls=[{"name": "task", "args": {"subagent_type": "citation-checker"}, "id": "5"}],
                  usage_metadata={"input_tokens": 12, "output_tokens": 7, "total_tokens": 19}),
        *(ToolMessage(content="completed", tool_call_id=call_id) for call_id in ("1", "2", "3", "5"))]


class FakeBackend:
    def __init__(self, report=None, sources=None, fail_command=None):
        self.files = {research.REPORT_PATH: report, research.SOURCES_PATH: sources}
        self.commands = []
        self.uploaded = {}
        self.fail_command = fail_command

    def execute(self, command, **kwargs):
        self.commands.append(command)
        if self.fail_command and self.fail_command in command and (self.fail_command in ("mkdir", "test -s") or command.startswith("python3 ")):
            return SimpleNamespace(exit_code=1, output="failed")
        if command.startswith("test -s"):
            return SimpleNamespace(exit_code=0 if all(self.uploaded.get(p) for p in (research.VALIDATOR_PATH, research.FINALIZER_PATH)) else 1, output="")
        if research.VALIDATOR_PATH in command:
            return SimpleNamespace(exit_code=0, output="OK: 3 sources, all citations resolve")
        return SimpleNamespace(exit_code=0, output="")

    def upload_files(self, files):
        self.uploaded.update(files)
        return [SimpleNamespace(path=p, error=None) for p, _ in files]

    def download_files(self, paths):
        return [SimpleNamespace(path=p, content=self.files.get(p), error=None) for p in paths]


class ResearchTests(unittest.TestCase):
    def test_slug_cannot_escape_and_is_bounded(self):
        for topic in ("", "   ", "../../x", "Mô hình thế giới!?", "a" * 100, "CON"):
            slug = research.slugify(topic)
            self.assertTrue(slug)
            self.assertLessEqual(len(slug), 60)
            self.assertNotIn("/", slug)
            self.assertNotIn("\\", slug)
            self.assertNotIn("..", slug)
        self.assertEqual(research.slugify(""), "topic")

    def test_prompt_has_current_asia_saigon_date_and_output_contract(self):
        with patch.object(research, "datetime") as clock:
            clock.now.return_value = datetime(2026, 10, 9, 12, 0, tzinfo=timezone(timedelta(hours=7)))
            prompt = research.build_prompt("world models")
            self.assertEqual(clock.now.call_args.args[0].utcoffset(None), timedelta(hours=7))
        self.assertIn("world models", prompt)
        self.assertIn("2026-10-09", prompt)
        self.assertIn("English", prompt)
        self.assertIn("3-6", prompt)
        self.assertIn("source", prompt.lower())

    def test_cli_parses_quoted_and_unquoted_topics_with_review_feedback(self):
        for argv in (["video world models", "--review-feedback", "wrong citation"],
                     ["video", "world", "models", "--review-feedback", "wrong citation"]):
            with self.subTest(argv=argv):
                self.assertEqual(research.parse_cli(argv), ("video world models", "wrong citation"))
        self.assertEqual(research.parse_cli([]), ("", ""))

    def test_review_feedback_reaches_initial_prompt_without_changing_topic_or_metadata(self):
        report, sources = fixture()
        backend = FakeBackend(report, sources)
        topic = "Video world models"
        prompts = []

        class Agent:
            def invoke(self, payload, config):
                prompts.append(payload["messages"][0]["content"])
                return {"messages": messages()}

        @contextmanager
        def sandbox():
            yield backend

        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"REVIEW_API_KEY": "private-value"}), patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
            self.assertEqual(research.main(topic, "VideoGPT cites wrong [2]; api_key=private-value\nDreamFoley cites wrong [9]."), 0)
            self.assertEqual(len(prompts), 1)
            self.assertIn("Reviewer feedback", prompts[0])
            self.assertIn("VideoGPT cites wrong [2]", prompts[0])
            self.assertIn("DreamFoley cites wrong [9]", prompts[0])
            self.assertNotIn("private-value", prompts[0])
            self.assertIn("[REDACTED]", prompts[0])
            meta = json.loads((Path(tmp) / "video-world-models.meta.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["topic"], topic)
            self.assertEqual((Path(tmp) / "video-world-models.md").read_bytes(), report)

    def test_summarize_counts_only_supplied_lead_messages(self):
        meta = research.summarize(messages(), 2.36, "gpt-test")
        self.assertEqual(meta["elapsed_s"], 2.4)
        self.assertEqual(meta["subagent_calls"], 4)
        self.assertEqual(meta["tool_calls"], {"task": 4, "write_todos": 1})
        self.assertEqual(meta["tokens"], {"input": 22, "output": 12})
        self.assertEqual(meta["researcher_calls"], 3)
        self.assertEqual(meta["checker_calls"], 1)
        self.assertEqual(meta["max_parallel_researchers"], 3)
        self.assertEqual(meta["successful_researcher_calls"], 3)
        self.assertEqual(meta["successful_checker_calls"], 1)
        sequential = [AIMessage(content="", tool_calls=[{"name": "task", "args": {"subagent_type": "researcher"}, "id": str(i)}]) for i in range(3)]
        self.assertEqual(research.summarize(sequential, 1, "x")["max_parallel_researchers"], 1)

    def test_save_preserves_downloaded_bytes_and_writes_true_metadata(self):
        report, sources = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            path = research.save_outputs(FakeBackend(report, sources), "World models", messages(), 2.36, "gpt-test", Path(tmp))
            self.assertEqual(path.read_bytes(), report)
            self.assertEqual(path.with_suffix(".sources.json").read_bytes(), sources)
            meta = json.loads(path.with_suffix(".meta.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["topic"], "World models")
            self.assertEqual(meta["n_sources"], 3)
            self.assertEqual(meta["source_families"], ["arxiv", "hf-search", "web"])
            self.assertEqual(meta["tokens"], {"input": 22, "output": 12})
            self.assertEqual((meta["successful_researcher_calls"], meta["successful_checker_calls"]), (3, 1))

    def test_task_result_gate_rejects_missing_failed_and_unmatched_results(self):
        report, sources = fixture()
        base = messages()
        cases = {
            "missing all": base[:3],
            "all researchers failed": base[:3] + [
                ToolMessage(content="ERROR: task failed", tool_call_id=call_id)
                for call_id in ("1", "2", "3")
            ] + base[-1:],
            "researcher status error": base[:3] + [ToolMessage(content="failed", tool_call_id="1", status="error")] + base[4:],
            "researcher content error": base[:3] + [ToolMessage(content="ERROR: failed", tool_call_id="1")] + base[4:],
            "checker content error": base[:-1] + [ToolMessage(content="Error: failed", tool_call_id="5")],
            "checker status error": base[:-1] + [ToolMessage(content="failed", tool_call_id="5", status="error")],
            "unmatched id": base[:3] + [ToolMessage(content="completed", tool_call_id="other")] + base[4:],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for label, history in cases.items():
                with self.subTest(label=label):
                    with self.assertRaisesRegex(RuntimeError, "successful"):
                        research.save_outputs(FakeBackend(report, sources), "test", history, 1, "x", root)
                    self.assertEqual(list(root.iterdir()), [])

    def test_successful_task_counts_ignore_duplicate_results(self):
        history = messages() + [ToolMessage(content="completed again", tool_call_id="1")]
        meta = research.summarize(history, 1, "x")
        self.assertEqual((meta["successful_researcher_calls"], meta["successful_checker_calls"]), (3, 1))

    def test_invalid_download_never_replaces_good_trio(self):
        report, sources = fixture()
        cases = [(None, sources), (b"", sources), (report, None), (report, b"{"),
                 (report, b"[]"), (report, json.dumps([{"n": 1}]).encode()),
                 (report.replace(b"## Evaluation", b"Evaluation"), sources),
                 (report.replace(b"## Trends and open problems", b"## Missing final section"), sources)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = {suffix: b"old-good" for suffix in (".md", ".sources.json", ".meta.json")}
            for suffix, data in old.items():
                (root / f"test{suffix}").write_bytes(data)
            for bad_report, bad_sources in cases:
                with self.subTest(report=bad_report is not None, sources=bad_sources):
                    with self.assertRaises((RuntimeError, ValueError)) as error:
                        research.save_outputs(FakeBackend(bad_report, bad_sources), "test", messages(), 1, "x", root)
                    self.assertNotIsInstance(error.exception, NotImplementedError)
                    for suffix, data in old.items():
                        self.assertEqual((root / f"test{suffix}").read_bytes(), data)

    def test_save_requires_parallel_research_and_a_checker_call(self):
        report, sources = fixture()
        serial = [AIMessage(content="", tool_calls=[{
            "name": "task", "args": {"subagent_type": "researcher"}, "id": str(i)
        }]) for i in range(3)] + messages()[-1:]
        cases = [serial, messages()[:2], [messages()[-1]] * 4]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for invalid in cases:
                with self.subTest(messages=len(invalid)):
                    with self.assertRaises(RuntimeError):
                        research.save_outputs(FakeBackend(report, sources), "test", invalid, 1, "x", root)
                    self.assertEqual(list(root.iterdir()), [])

    def test_empty_required_or_theme_sections_are_rejected_even_if_tldr_has_all_citations(self):
        report, sources = fixture()
        removals = [b"Context [1].", b"Comparison [1][2].", b"Results [2][3].", b"Gaps [3].", b"Trend [1][3]."]
        with tempfile.TemporaryDirectory() as tmp:
            for body in removals:
                with self.subTest(body=body):
                    with self.assertRaisesRegex(RuntimeError, "empty"):
                        research.save_outputs(FakeBackend(report.replace(body, b"   "), sources), "test", messages(), 1, "x", Path(tmp))
                    self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_tldr_requires_three_to_five_cited_bullets(self):
        report, sources = fixture()
        too_few = report.replace(b"- Finding B [2].\n- Finding C [3].\n", b"")
        uncited = report.replace(b"- Finding B [2].", b"- Finding B without citation.")
        with tempfile.TemporaryDirectory() as tmp:
            for invalid in (too_few, uncited):
                with self.subTest(invalid=invalid):
                    with self.assertRaisesRegex(RuntimeError, "TL;DR"):
                        research.save_outputs(FakeBackend(invalid, sources), "test", messages(), 1, "x", Path(tmp))
                    self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_second_destination_failure_rolls_back_first(self):
        report, sources = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = [root / f"test{suffix}" for suffix in (".md", ".sources.json", ".meta.json")]
            for path in paths:
                path.write_bytes(b"prior")
            real_replace = os.replace
            state = {"failed": False}

            def fail_once(src, dst):
                if Path(dst) == paths[1] and not state["failed"]:
                    state["failed"] = True
                    raise OSError("disk error")
                return real_replace(src, dst)

            with patch.object(research.os, "replace", side_effect=fail_once):
                with self.assertRaises(OSError):
                    research.save_outputs(FakeBackend(report, sources), "test", messages(), 1, "x", root)
            self.assertTrue(state["failed"])
            self.assertEqual([p.read_bytes() for p in paths], [b"prior"] * 3)

    def test_main_lifecycle_and_cleanup_on_agent_failure(self):
        report, sources = fixture()
        backend = FakeBackend(report, sources)
        state = {"closed": False, "invoked": False}

        @contextmanager
        def sandbox():
            try:
                yield backend
            finally:
                state["closed"] = True

        class Agent:
            def invoke(self, payload, config):
                state["invoked"] = True
                assert config["recursion_limit"] == 1000
                assert len(config["callbacks"]) == 1
                assert "world models" in payload["messages"][0]["content"]
                return {"messages": messages()}

        with tempfile.TemporaryDirectory() as tmp, patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="gpt-test")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
            self.assertEqual(research.main("world models"), 0)
            self.assertTrue(state["closed"])
            self.assertTrue(state["invoked"])
            self.assertTrue((Path(tmp) / "world-models.md").exists())
            self.assertEqual(backend.uploaded[research.VALIDATOR_PATH], research.VALIDATOR_SOURCE.read_bytes())
            self.assertEqual(backend.uploaded[research.FINALIZER_PATH], research.FINALIZER_SOURCE.read_bytes())
            self.assertLess(next(i for i, c in enumerate(backend.commands) if c.startswith("python3 ") and research.FINALIZER_PATH in c), next(i for i, c in enumerate(backend.commands) if c.startswith("python3 ") and research.VALIDATOR_PATH in c))

    def test_main_repairs_failed_output_once_with_complete_history(self):
        good_report, sources = fixture()
        bad_report = good_report.replace(b"Comparison [1][2].", b"   ")
        backend = FakeBackend(bad_report, sources)
        first_history = messages()
        repaired_history = first_history + [AIMessage(content="repaired", usage_metadata={
            "input_tokens": 1, "output_tokens": 2, "total_tokens": 3})]
        payloads = []

        class Agent:
            def invoke(self, payload, config):
                payloads.append(payload["messages"])
                if len(payloads) == 1:
                    return {"messages": first_history}
                backend.files[research.REPORT_PATH] = good_report
                return {"messages": repaired_history}

        @contextmanager
        def sandbox():
            yield backend

        with tempfile.TemporaryDirectory() as tmp, patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
            self.assertEqual(research.main("test"), 0)
            self.assertEqual(len(payloads), 2)
            self.assertEqual(payloads[1][:-1], first_history)
            self.assertEqual(len(first_history), len(messages()))
            self.assertIn("empty Methods section", payloads[1][-1]["content"])
            self.assertIn("citation-checker", payloads[1][-1]["content"])
            self.assertEqual([c for c in backend.commands if c.startswith("python3 ")],
                             [f"python3 {research.FINALIZER_PATH}", f"python3 {research.VALIDATOR_PATH}"] * 2)
            path = Path(tmp) / "test.md"
            self.assertEqual(path.read_bytes(), good_report)
            meta = json.loads(path.with_suffix(".meta.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["tool_calls"], {"task": 4, "write_todos": 1})
            self.assertEqual(meta["tokens"], {"input": 23, "output": 14})

    def test_main_stops_after_one_failed_repair_and_preserves_old_trio(self):
        good_report, sources = fixture()
        backend = FakeBackend(good_report.replace(b"Comparison [1][2].", b"   "), sources)
        invocations = []

        class Agent:
            def invoke(self, payload, config):
                invocations.append(payload)
                return {"messages": messages()}

        @contextmanager
        def sandbox():
            yield backend

        with tempfile.TemporaryDirectory() as tmp, patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
            root = Path(tmp)
            old = {suffix: b"old-good" for suffix in (".md", ".sources.json", ".meta.json")}
            for suffix, data in old.items():
                (root / f"test{suffix}").write_bytes(data)
            self.assertEqual(research.main("test"), 1)
            self.assertEqual(len(invocations), 2)
            for suffix, data in old.items():
                self.assertEqual((root / f"test{suffix}").read_bytes(), data)

    def test_main_does_not_retry_download_backend_failure(self):
        class BrokenDownloadBackend(FakeBackend):
            def download_files(self, paths):
                raise RuntimeError("backend download unavailable")

        backend = BrokenDownloadBackend(*fixture())
        invocations = []
        closed = []

        class Agent:
            def invoke(self, payload, config):
                invocations.append(payload)
                return {"messages": messages()}

        @contextmanager
        def sandbox():
            try:
                yield backend
            finally:
                closed.append(True)

        with tempfile.TemporaryDirectory() as tmp, patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
            root = Path(tmp)
            old = {suffix: b"old-good" for suffix in (".md", ".sources.json", ".meta.json")}
            for suffix, data in old.items():
                (root / f"test{suffix}").write_bytes(data)
            self.assertEqual(research.main("test"), 1)
            self.assertEqual(len(invocations), 1)
            self.assertTrue(closed)
            for suffix, data in old.items():
                self.assertEqual((root / f"test{suffix}").read_bytes(), data)

    def test_main_rejects_empty_and_failed_sandbox_commands(self):
        with patch.object(research, "make_model", side_effect=AssertionError("must not initialize")):
            self.assertEqual(research.main("   "), 2)
        for failed in ("mkdir", "test -s", research.FINALIZER_PATH, research.VALIDATOR_PATH):
            with self.subTest(failed=failed), tempfile.TemporaryDirectory() as tmp:
                backend = FakeBackend(*fixture(), fail_command=failed)
                closed = []

                @contextmanager
                def sandbox():
                    try:
                        yield backend
                    finally:
                        closed.append(True)

                class Agent:
                    def invoke(self, *args, **kwargs):
                        return {"messages": messages()}

                with patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()):
                    self.assertEqual(research.main("test"), 1)
                self.assertTrue(closed)
                self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_agent_exception_returns_one_and_cleans_up(self):
        backend = FakeBackend(*fixture())
        closed = []

        @contextmanager
        def sandbox():
            try:
                yield backend
            finally:
                closed.append(True)

        class Agent:
            def invoke(self, *args, **kwargs):
                raise RuntimeError("api_key=secret-value")

        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"LAB_API_KEY": "secret-value"}), patch.object(research, "REPORTS", Path(tmp)), patch.object(research, "make_model", return_value=SimpleNamespace(model_name="x")), patch.object(research, "open_sandbox", sandbox), patch.object(research, "build_lead_agent", return_value=Agent()), patch("sys.stderr") as stderr:
            self.assertEqual(research.main("test"), 1)
            self.assertTrue(closed)
            self.assertEqual(list(Path(tmp).iterdir()), [])
            self.assertNotIn("secret-value", "".join(str(call) for call in stderr.write.call_args_list))

    def test_progress_callback_prints_only_tool_name(self):
        from contextlib import redirect_stdout
        output = StringIO()
        with redirect_stdout(output):
            research.ToolProgress().on_tool_start({"name": "task"}, "api_key=secret-value")
        self.assertIn("task", output.getvalue())
        self.assertNotIn("secret-value", output.getvalue())


if __name__ == "__main__":
    unittest.main()
