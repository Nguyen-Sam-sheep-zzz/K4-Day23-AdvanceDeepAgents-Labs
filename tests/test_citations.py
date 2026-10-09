"""Behavior tests for the sandbox citation gate (no network or mocks)."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from check_citations import check


SOURCE = {"n": 1, "url": "https://example.org/paper"}
REFERENCE = "[1] Paper. web. https://example.org/paper (2026-01-01)\n"
REPORT = "# Survey\nA supported claim [1].\n\n## References\n" + REFERENCE


class CitationTests(unittest.TestCase):
    def assert_problem(self, report, sources, fragment):
        problems = check(report, sources)
        self.assertTrue(problems, "invalid input was accepted")
        self.assertTrue(any(fragment in p for p in problems), problems)

    def test_valid_report(self):
        self.assertEqual(check(REPORT, [SOURCE]), [])

    def test_sources_must_be_nonempty_json_array(self):
        for sources in (None, {}, "sources", 3, [], [None], ["source"]):
            with self.subTest(sources=sources):
                self.assert_problem(REPORT, sources, "source")

    def test_source_number_is_positive_integer_not_boolean(self):
        for n in (None, "1", 1.0, True, False, 0, -1, []):
            with self.subTest(n=n):
                self.assert_problem(REPORT, [{"n": n, "url": SOURCE["url"]}], "n")

    def test_duplicate_source_numbers_rejected(self):
        self.assert_problem(REPORT, [SOURCE, {"n": 1, "url": "https://other.org"}], "duplicate n")

    def test_source_url_must_be_valid_http_url(self):
        for url in (None, [], 5, "ftp://example.org", "https://", "https:///bad", "https://example.org/a b"):
            with self.subTest(url=url):
                self.assert_problem(REPORT, [{"n": 1, "url": url}], "url")

    def test_duplicate_source_urls_rejected(self):
        self.assert_problem(REPORT, [SOURCE, {"n": 2, "url": SOURCE["url"]}], "duplicate url")

    def test_missing_references_heading(self):
        self.assert_problem("Claim [1]", [SOURCE], "References")

    def test_fake_heading_in_fenced_or_inline_code_does_not_split_body(self):
        for code in ("```markdown\n## References\n```", "~~~\n## References\n~~~", "`## References`"):
            with self.subTest(code=code):
                self.assertEqual(check(code + "\n" + REPORT, [SOURCE]), [])
                self.assert_problem(code + "\nClaim [1]", [SOURCE], "References")

    def test_reference_numbers_are_not_body_citations(self):
        self.assert_problem("# Survey\nNo citation.\n## References\n" + REFERENCE, [SOURCE], "never cited")

    def test_code_and_markdown_links_are_not_citations(self):
        for body in (
            "```\n[1]\n```", "~~~python\n[1]\n~~~", "`[1]`", "``a `[1]` b``",
            "[1](https://example.org)", "![1](https://example.org)",
            "[1][paper]\n\n[paper]: https://example.org", "\\[1]",
        ):
            with self.subTest(body=body):
                self.assert_problem(body + "\n## References\n" + REFERENCE, [SOURCE], "never cited")

    def test_ignored_code_or_links_cannot_introduce_unknown_citations(self):
        noise = "`[99]` [99](https://example.org)\n```\n[98]\n```\n"
        self.assertEqual(check(noise + REPORT, [SOURCE]), [])

    def test_inline_code_can_span_multiple_lines(self):
        self.assert_problem("`code\n[1]`\n## References\n" + REFERENCE, [SOURCE], "never cited")

    def test_escaped_backticks_do_not_hide_a_real_citation(self):
        self.assertEqual(check("Literal \\` claim [1] \\`\n## References\n" + REFERENCE, [SOURCE]), [])

    def test_reference_definition_does_not_create_a_citation(self):
        for body in ("[1]: https://example.org", "[1][]\n\n[1]: https://example.org"):
            with self.subTest(body=body):
                self.assert_problem(body + "\n## References\n" + REFERENCE, [SOURCE], "never cited")

    def test_markdown_link_nested_label_does_not_create_a_citation(self):
        self.assert_problem("[See [1]](https://example.org/path_(one))\n## References\n" + REFERENCE, [SOURCE], "never cited")

    def test_unknown_body_citation(self):
        self.assert_problem(REPORT.replace("claim [1]", "claim [1][2]"), [SOURCE], "[2] cited but missing")

    def test_grouped_and_ranged_citations(self):
        sources = [SOURCE, {"n": 2, "url": "https://example.org/two"}, {"n": 3, "url": "https://example.org/three"}]
        refs = REFERENCE + "[2] Two. https://example.org/two\n[3] Three. https://example.org/three\n"
        for citation in ("[1, 2, 3]", "[1-3]", "[1–3]", "[1, 2-3]", "[1][2][3]"):
            with self.subTest(citation=citation):
                self.assertEqual(check("Claim " + citation + "\n## References\n" + refs, sources), [])

    def test_invalid_or_unbounded_range_is_a_problem_not_a_hang(self):
        for citation in ("[3-1]", "[0]", "[1-10000000000000000000000]", "[" + "9" * 5000 + "]"):
            with self.subTest(citation=citation[:60]):
                self.assert_problem(citation + "\n" + REPORT, [SOURCE], "citation")

    def test_missing_reference_entry(self):
        self.assert_problem(REPORT.replace(REFERENCE, ""), [SOURCE], "reference")

    def test_duplicate_reference_entry(self):
        self.assert_problem(REPORT + REFERENCE, [SOURCE], "reference")

    def test_reference_entry_with_unknown_number(self):
        self.assert_problem(REPORT + "[2] Two. https://example.org/two\n", [SOURCE], "[2]")

    def test_reference_url_must_match_source(self):
        self.assert_problem(REPORT.replace("https://example.org/paper", "https://example.org/other"), [SOURCE], "url")

    def test_reference_must_have_exactly_one_url(self):
        for reference in ("[1] No URL.\n", REFERENCE.rstrip() + " https://other.org\n", REFERENCE.rstrip() + " https://example.org/paper\n"):
            with self.subTest(reference=reference):
                self.assert_problem(REPORT.replace(REFERENCE, reference), [SOURCE], "URL")

    def test_reference_url_can_be_wrapped_in_markdown(self):
        for url in ("<https://example.org/paper>", "[Paper](https://example.org/paper)"):
            with self.subTest(url=url):
                self.assertEqual(check(REPORT.replace(SOURCE["url"], url), [SOURCE]), [])

    def test_parentheses_inside_url_preserved(self):
        source = {"n": 1, "url": "https://example.org/paper_(one)"}
        self.assertEqual(check(REPORT.replace(SOURCE["url"], "[Paper](https://example.org/paper_(one))"), [source]), [])

    def test_references_is_single_final_section(self):
        for tail in ("## Conclusion\nClaim [1]\n", "An extra claim [1].\n", "## References\n" + REFERENCE, "```\n[2]\n```\n"):
            with self.subTest(tail=tail):
                self.assert_problem(REPORT + tail, [SOURCE], "References")

    def test_malformed_report_type_returns_problem(self):
        self.assert_problem(None, [SOURCE], "report")

    def test_cli_success_and_invalid_inputs(self):
        script = Path(__file__).resolve().parents[1] / "check_citations.py"
        with tempfile.TemporaryDirectory() as temporary:
            report = Path(temporary) / "report.md"
            sources = Path(temporary) / "sources.json"
            report.write_text(REPORT, encoding="utf-8")
            sources.write_text(json.dumps([SOURCE]), encoding="utf-8")
            result = subprocess.run([sys.executable, str(script), str(report), str(sources)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("OK: 1 sources", result.stdout)
            for content in ("{", "null", "[]"):
                with self.subTest(content=content):
                    sources.write_text(content, encoding="utf-8")
                    result = subprocess.run([sys.executable, str(script), str(report), str(sources)], capture_output=True, text=True)
                    self.assertEqual(result.returncode, 1, result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
            result = subprocess.run([sys.executable, str(script), str(report) + ".missing", str(sources)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("cannot read inputs", result.stdout)


if __name__ == "__main__":
    unittest.main()
