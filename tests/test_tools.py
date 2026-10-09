"""Offline contract checks for the five host-side source tools."""
import json
import unittest
from unittest.mock import patch

import httpx

import tools


def response(status=200, text="", headers=None, url="https://example.org"):
    return httpx.Response(status, text=text, headers=headers, request=httpx.Request("GET", url))


class RetryTests(unittest.TestCase):
    def test_retryable_failure_then_success_and_retry_after(self):
        calls = 0

        def operation():
            nonlocal calls
            calls += 1
            if calls == 1:
                raise tools.RetryableError("busy", retry_after=7)
            return "ok"

        with patch.object(tools.time, "sleep") as sleep:
            self.assertEqual(tools.with_retry(operation, attempts=3), "ok")
        self.assertEqual(calls, 2)
        sleep.assert_called_once_with(7)

    def test_final_failure_does_not_sleep_and_programming_error_is_not_retried(self):
        with patch.object(tools.time, "sleep") as sleep:
            with self.assertRaises(tools.RetryableError):
                tools.with_retry(lambda: (_ for _ in ()).throw(tools.RetryableError("busy")), attempts=1)
            with self.assertRaises(ValueError):
                tools.with_retry(lambda: (_ for _ in ()).throw(ValueError("bad")), attempts=3)
        sleep.assert_not_called()

    def test_exponential_backoff_has_jitter_and_cap(self):
        with patch.object(tools.time, "sleep") as sleep, patch.object(tools.random, "uniform", return_value=0.25):
            with self.assertRaises(tools.RetryableError):
                tools.with_retry(lambda: (_ for _ in ()).throw(tools.RetryableError("busy")), attempts=4, base=2, cap=5)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [2.25, 4.25, 5])

    def test_http_429_retry_after_503_and_transport_timeout_are_retried(self):
        for first in (response(429, headers={"Retry-After": "4"}), response(503), httpx.ConnectTimeout("temporary")):
            calls = 0

            def get(*args, **kwargs):
                nonlocal calls
                calls += 1
                if calls == 1:
                    if isinstance(first, Exception):
                        raise first
                    return first
                return response(text="[]")

            with self.subTest(first=first), patch.object(tools.httpx, "get", side_effect=get), patch.object(tools.time, "sleep") as sleep:
                self.assertEqual(tools.hf_daily_papers.invoke({}), "NO RESULTS")
                self.assertEqual(calls, 2)
                if isinstance(first, httpx.Response) and first.status_code == 429:
                    sleep.assert_called_once_with(4)

    def test_http_400_does_not_retry_and_bad_json_is_error(self):
        with patch.object(tools.httpx, "get", return_value=response(400)) as get:
            self.assertTrue(tools.hf_daily_papers.invoke({}).startswith("ERROR:"))
            self.assertEqual(get.call_count, 1)
        with patch.object(tools.httpx, "get", return_value=response(text="not JSON")):
            self.assertTrue(tools.hf_daily_papers.invoke({}).startswith("ERROR:"))


class ArxivTests(unittest.TestCase):
    def test_query_is_sanitized_and_atom_is_normalized(self):
        xml = '''<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/abs/cs/9901001v3</id><published>2025-02-01T01:02:03Z</published><title>  A  title\n here </title><summary>Line  one\n two</summary></entry></feed>'''
        with patch.object(tools.httpx, "get", return_value=response(text=xml)) as get, patch.object(tools.time, "sleep"):
            result = json.loads(tools.arxiv_search.invoke({"query": '"world" AND model OR graph', "max_results": 99}))
        self.assertEqual(get.call_args.kwargs["params"]["search_query"], "all:world AND all:model AND all:graph")
        self.assertEqual(get.call_args.kwargs["params"]["max_results"], 30)
        self.assertEqual(result[0]["id"], "cs/9901001")
        self.assertEqual(result[0]["url"], "https://arxiv.org/abs/cs/9901001")
        self.assertEqual(result[0]["title"], "A title here")

    def test_empty_query_skips_network(self):
        with patch.object(tools.httpx, "get") as get:
            self.assertEqual(tools.arxiv_search.invoke({"query": "AND OR !!"}), "NO RESULTS")
        get.assert_not_called()

    def test_error_feed_never_creates_paper_from_non_abs_url(self):
        xml = '''<feed xmlns="http://www.w3.org/2005/Atom"><entry><id>http://arxiv.org/api/errors</id><title>Search error</title></entry></feed>'''
        with patch.object(tools.httpx, "get", return_value=response(text=xml)), patch.object(tools.time, "sleep"):
            result = tools.arxiv_search.invoke({"query": "world"})
        self.assertEqual(result, "NO RESULTS")

    def test_malformed_atom_returns_error_string(self):
        with patch.object(tools.httpx, "get", return_value=response(text="<feed><entry>")), patch.object(tools.time, "sleep"):
            self.assertTrue(tools.arxiv_search.invoke({"query": "world"}).startswith("ERROR:"))

    def test_arxiv_retry_preserves_three_second_request_spacing(self):
        clock = [100.0]
        request_times = []
        xml = '<feed xmlns="http://www.w3.org/2005/Atom"/>'

        def sleep(seconds):
            clock[0] += seconds

        def get(*args, **kwargs):
            request_times.append(clock[0])
            return response(429) if len(request_times) == 1 else response(text=xml)

        with patch.object(tools, "_ARXIV_LAST_CALL", 0.0), patch.object(tools.time, "monotonic", side_effect=lambda: clock[0]), patch.object(tools.time, "sleep", side_effect=sleep), patch.object(tools.random, "uniform", return_value=0.25), patch.object(tools.httpx, "get", side_effect=get):
            self.assertEqual(tools.arxiv_search.invoke({"query": "world"}), "NO RESULTS")
        self.assertEqual(request_times, [100.0, 103.0])


class HuggingFaceTests(unittest.TestCase):
    def test_daily_filters_sorts_and_handles_nested_and_top_fields(self):
        items = [
            {"paper": {"id": "a", "title": "World model", "summary": "first", "upvotes": 2, "publishedAt": "2025-01-01", "githubRepo": "repo", "githubStars": 3}},
            {"paper": {"id": "b", "title": "Other", "summary": "x", "upvotes": 99}},
            {"paper": {"id": "c"}, "title": "World models", "summary": "top summary", "upvotes": 5},
            {"title": "World model"},
        ]
        with patch.object(tools.httpx, "get", return_value=response(text=json.dumps(items))):
            result = json.loads(tools.hf_daily_papers.invoke({"keyword": "world"}))
        self.assertEqual([record["id"] for record in result], ["c", "a"])
        self.assertEqual(result[0]["summary"], "top summary")
        self.assertEqual(result[1]["github"], "repo")

    def test_search_prefers_ai_summary(self):
        items = [{"paper": {"id": "x", "summary": "raw", "ai_summary": "AI summary", "title": "Paper"}}]
        with patch.object(tools.httpx, "get", return_value=response(text=json.dumps(items))):
            result = json.loads(tools.hf_search_papers.invoke({"query": "model"}))
        self.assertEqual(result[0]["summary"], "AI summary")

    def test_top_level_id_without_paper_is_skipped(self):
        items = [{"id": "top-only", "title": "Invalid"}, {"paper": {"id": "valid", "title": "Valid"}}]
        with patch.object(tools.httpx, "get", return_value=response(text=json.dumps(items))):
            result = json.loads(tools.hf_search_papers.invoke({"query": "model"}))
        self.assertEqual([record["id"] for record in result], ["valid"])


class ExaTests(unittest.TestCase):
    def test_search_reads_sse_and_supplies_objective(self):
        payload = {"jsonrpc": "2.0", "id": 1, "result": {"content": [{"type": "text", "text": "Useful page https://example.org"}]}}
        sse = f'event: message\ndata: {json.dumps(payload)}\n\n'
        with patch.object(tools.httpx, "post", return_value=response(text=sse)) as post:
            self.assertIn("Useful page", tools.web_search.invoke({"query": "world models"}))
        body = post.call_args.kwargs["json"]
        self.assertEqual(body["params"]["arguments"]["query"], "world models")
        self.assertTrue(body["params"]["arguments"]["objective"])
        self.assertIn("text/event-stream", post.call_args.kwargs["headers"]["Accept"])

    def test_fetch_sends_url_array_and_truncates(self):
        payload = {"result": {"content": [{"type": "text", "text": "x" * 13000}]}}
        with patch.object(tools.httpx, "post", return_value=response(text=json.dumps(payload))) as post:
            result = tools.web_fetch.invoke({"url": "https://example.org"})
        self.assertEqual(len(result), 12000)
        self.assertEqual(post.call_args.kwargs["json"]["params"]["arguments"]["urls"], ["https://example.org"])

    def test_http_200_rpc_rate_limit_is_not_content(self):
        payload = {"result": {"isError": True, "_meta": {"isRateLimited": True}, "content": [{"type": "text", "text": "rate limit"}]}}
        with patch.object(tools.httpx, "post", return_value=response(text=json.dumps(payload))) as post, patch.object(tools.time, "sleep"):
            result = tools.web_search.invoke({"query": "topic"})
        self.assertTrue(result.startswith("ERROR:"))
        self.assertNotIn("rate limit\n", result)
        self.assertGreater(post.call_count, 1)

    def test_metadata_rate_limit_retries_even_without_iserror(self):
        payload = {"result": {"_meta": {"isRateLimited": True}, "content": [{"type": "text", "text": "Please wait"}]}}
        with patch.object(tools.httpx, "post", return_value=response(text=json.dumps(payload))) as post, patch.object(tools.time, "sleep"):
            self.assertTrue(tools.web_search.invoke({"query": "topic"}).startswith("ERROR:"))
        self.assertGreater(post.call_count, 1)

    def test_auth_failure_is_not_retried_and_secrets_are_redacted(self):
        secret = "secret-" * 5
        leaked_url = f"https://mcp.exa.ai/mcp?exaApiKey={secret}"
        with patch.dict(tools.os.environ, {"EXA_API_KEY": secret}), patch.object(tools.httpx, "post", return_value=response(401, url=leaked_url)) as post:
            result = tools.web_search.invoke({"query": "topic"})
        self.assertTrue(result.startswith("ERROR:"))
        self.assertNotIn(secret, result)
        self.assertEqual(post.call_count, 1)


if __name__ == "__main__":
    unittest.main()
