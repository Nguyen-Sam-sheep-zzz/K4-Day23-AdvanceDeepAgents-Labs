# Task 2: Source tools verification

Implemented `with_retry`, arXiv, Hugging Face Daily/Search, and Exa Search/Fetch in `tools.py`. All source tools return a string: compact source data, `NO RESULTS`, or a redacted `ERROR: ...` on failure. Retry is limited to `RetryableError`, which the network wrapper raises for HTTP 429/500/502/503/504 and transport failures. ArXiv requests use a shared lock and at least three seconds between attempts, including retries. Exa parses JSON and SSE JSON-RPC, handles result errors and rate-limit metadata, and sends the documented search/fetch arguments.

Offline verification: `.venv/Scripts/python.exe -m unittest discover -s tests -p test_tools.py -v` passed 18 tests. Coverage includes Retry-After, exponential backoff with cap and jitter, final-attempt behavior, HTTP 400 without retry, HTTP 429/503 and connection timeout with retry, Atom normalization and request spacing, Hugging Face nested/top field handling, SSE and JSON replies, rate-limit metadata under HTTP 200, fetch truncation, malformed responses, and error redaction.

Endpoint probes shared by the integration task found HTTP 200 responses for both Hugging Face endpoints, and HTTP 429 for arXiv and Exa during that window. Those probes checked endpoint availability and response shape; they did not prove all five implemented tools could return research content live. A bounded live `python tools.py` smoke and final source-by-source results remain with the integration task. A rate-limited result is an error, never usable source evidence.

## Parent integration live checks

Bounded smoke used the real tools with one retry attempt per request, to report endpoint availability without waiting on known quotas. HF daily returned 3 records; HF search returned 3 records; web_search returned 6566 characters; web_fetch returned 12000 characters with the configured Exa key. arxiv_search returned `ERROR: RetryableError: HTTP 429`. This does not claim all five sources were healthy. Offline retry policy remained unchanged. Model gpt-6-luna tool calling succeeded (82 token smoke).
