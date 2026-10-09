"""tools.py - STUDENT IMPLEMENTS.  Source tools for the research agents.   Guide: GUIDE.md, part 1.

Rules for every tool:
  * runs on the HOST (not in the sandbox): API keys must never enter the sandbox;
  * returns a STRING (JSON text of compact records) and NEVER raises:
        "NO RESULTS"  when the source answers with nothing,
        "ERROR: ..."  when the source keeps failing after the retries (the agent then tries another source);
  * the docstring is the tool description the LLM reads: keep it precise (what it does, what it returns, when to use it).
Try your tools without any agent:   python tools.py
"""
import json
import os
import random
import re
import threading
import time
import xml.etree.ElementTree as ET
from urllib.parse import quote, unquote

import httpx  # noqa: F401
from dotenv import load_dotenv
from langchain_core.tools import tool

# ---- constants (given) ----
ARXIV_URL = "https://export.arxiv.org/api/query"  # https only: http answers 301
HF_DAILY_URL = "https://huggingface.co/api/daily_papers"
HF_SEARCH_URL = "https://huggingface.co/api/papers/search"
EXA_URL = "https://mcp.exa.ai/mcp"
_ARXIV_LOCK = threading.Lock()
_ARXIV_LAST_CALL = 0.0
_RETRY_STATUS = {429, 500, 502, 503, 504}


class RetryableError(Exception):
    """Given. Raise it inside a call to ask with_retry to wait and try again (retry_after in seconds, optional)."""

    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after


def with_retry(fn, *, attempts=5, base=1.0, cap=30.0):
    """Retry only RetryableError with bounded delay and no sleep after final failure."""
    if attempts < 1 or base < 0 or cap < 0:
        raise ValueError("Invalid retry bounds")
    for attempt in range(attempts):
        try:
            return fn()
        except RetryableError as exc:
            if attempt == attempts - 1:
                raise
            if exc.retry_after is not None:
                delay = min(cap, max(0.0, float(exc.retry_after)))
            else:
                exponential = min(cap, base * 2**attempt)
                delay = min(cap, exponential + random.uniform(0, min(base, cap)))
            time.sleep(delay)


def _retry_after(response):
    raw = response.headers.get("Retry-After", "")
    try:
        return max(0.0, float(raw))
    except ValueError:
        return None


def _checked_response(response):
    if response.status_code in _RETRY_STATUS:
        raise RetryableError(f"HTTP {response.status_code}", _retry_after(response))
    response.raise_for_status()
    return response


def _network(fn, *, attempts=5, cap=30.0):
    def call():
        try:
            return _checked_response(fn())
        except httpx.TransportError as exc:
            raise RetryableError(f"Network {type(exc).__name__}") from exc

    return with_retry(call, attempts=attempts, cap=cap)


def _clean_text(value, limit=None):
    result = " ".join(str(value or "").split())
    return result[:limit] if limit else result


def _bounded(value, lower, upper):
    return max(lower, min(upper, int(value)))


def _redact(value):
    message = str(value)
    for key, secret in os.environ.items():
        if any(mark in key.upper() for mark in ("KEY", "TOKEN", "SECRET", "PASSWORD")) and len(secret) >= 6:
            message = message.replace(secret, "[REDACTED]")
            message = message.replace(quote(secret, safe=""), "[REDACTED]")
            message = message.replace(unquote(secret), "[REDACTED]")
    message = re.sub(r"(?i)(exaApiKey|api[_-]?key|access[_-]?token|password|secret)=([^&#\s]+)", r"\1=[REDACTED]", message)
    return message


def _error(exc):
    return f"ERROR: {type(exc).__name__}: {_redact(exc)}"


def _arxiv_get(params):
    global _ARXIV_LAST_CALL
    with _ARXIV_LOCK:
        wait = 3.0 - (time.monotonic() - _ARXIV_LAST_CALL)
        if wait > 0:
            time.sleep(wait)
        _ARXIV_LAST_CALL = time.monotonic()
        return httpx.get(ARXIV_URL, params=params, timeout=20.0)


def _records_or_empty(records):
    return json.dumps(records, ensure_ascii=False) if records else "NO RESULTS"


@tool
def arxiv_search(query: str, max_results: int = 10) -> str:
    """Search arXiv papers by keywords, newest first. Returns a JSON list of {id, url, published, title, summary}."""
    try:
        terms = [term for term in re.findall(r"[\w-]+", query or "", re.UNICODE)
                 if term.upper() not in {"AND", "OR", "NOT"} and term.strip("-")]
        if not terms:
            return "NO RESULTS"
        params = {"search_query": " AND ".join(f"all:{term}" for term in terms),
                  "sortBy": "submittedDate", "sortOrder": "descending", "start": 0,
                  "max_results": _bounded(max_results, 1, 30)}
        response = _network(lambda: _arxiv_get(params), attempts=6, cap=60.0)
        root = ET.fromstring(response.content)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        records = []
        for entry in root.findall("a:entry", ns):
            raw_id = _clean_text(entry.findtext("a:id", default="", namespaces=ns))
            if "/abs/" not in raw_id:
                continue
            paper_id = re.sub(r"v\d+$", "", raw_id.split("/abs/")[-1])
            if not paper_id or not re.fullmatch(r"[\w./-]+", paper_id):
                continue
            records.append({"id": paper_id, "url": f"https://arxiv.org/abs/{paper_id}",
                            "published": _clean_text(entry.findtext("a:published", default="", namespaces=ns))[:10],
                            "title": _clean_text(entry.findtext("a:title", default="", namespaces=ns)),
                            "summary": _clean_text(entry.findtext("a:summary", default="", namespaces=ns), 600)})
        return _records_or_empty(records)
    except Exception as exc:
        return _error(exc)


def _hf_records(items, *, prefer_ai=False):
    if not isinstance(items, list):
        raise ValueError("Invalid Hugging Face response")
    records = []
    for item in items:
        if not isinstance(item, dict):
            continue
        paper = item.get("paper")
        if not isinstance(paper, dict):
            continue
        paper_id = str(paper.get("id") or "").strip()
        if not paper_id:
            continue
        def field(name):
            return paper.get(name) or item.get(name)
        summary = (field("ai_summary") if prefer_ai else None) or field("summary")
        records.append({"id": paper_id, "url": f"https://huggingface.co/papers/{paper_id}",
                        "published": str(field("publishedAt") or "")[:10],
                        "title": _clean_text(field("title")), "summary": _clean_text(summary, 600),
                        "upvotes": int(field("upvotes") or 0), "github": field("githubRepo") or "",
                        "stars": int(field("githubStars") or 0)})
    return records


@tool
def hf_daily_papers(limit: int = 30, date: str = "", keyword: str = "") -> str:
    """Hugging Face Daily Papers = what is trending in AI research. Returns a JSON list of
    {id, url, published, title, summary, upvotes, github, stars} sorted by upvotes. `date` is YYYY-MM-DD (empty = latest).
    `keyword` filters title/summary; there is no topic search on this endpoint (use hf_search_papers for a topic)."""
    try:
        params = {"limit": _bounded(limit, 1, 100)}
        if date:
            params["date"] = date
        items = _network(lambda: httpx.get(HF_DAILY_URL, params=params, timeout=20.0)).json()
        records = _hf_records(items)
        if keyword.strip():
            term = keyword.strip().casefold()
            records = [record for record in records if term in (record["title"] + " " + record["summary"]).casefold()]
        records.sort(key=lambda record: record["upvotes"], reverse=True)
        return _records_or_empty(records)
    except Exception as exc:
        return _error(exc)


@tool
def hf_search_papers(query: str, limit: int = 10) -> str:
    """Search Hugging Face papers by topic. Returns a JSON list of
    {id, url, published, title, summary, upvotes, github, stars}."""
    try:
        if not query or not query.strip():
            return "NO RESULTS"
        params = {"q": query.strip(), "limit": _bounded(limit, 1, 50)}
        items = _network(lambda: httpx.get(HF_SEARCH_URL, params=params, timeout=20.0)).json()
        return _records_or_empty(_hf_records(items, prefer_ai=True))
    except Exception as exc:
        return _error(exc)


def _exa_payload(text):
    if text.lstrip().startswith("{"):
        return json.loads(text)
    for line in text.splitlines():
        if line.startswith("data:"):
            data = line[5:].strip()
            if data and data != "[DONE]":
                return json.loads(data)
    raise ValueError("Invalid Exa response")


def _rate_limited(payload):
    meta = payload.get("_meta") or {}
    if isinstance(meta, dict):
        for key, value in meta.items():
            if "ratelimit" in key.lower().replace("_", "").replace("-", "") and value is True:
                return True
    return False


def _exa_call(name, arguments):
    key = os.getenv("EXA_API_KEY", "")
    url = EXA_URL + ("?exaApiKey=" + quote(key, safe="") if key else "")
    request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
               "params": {"name": name, "arguments": arguments}}
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

    def call():
        response = _network(lambda: httpx.post(url, json=request, headers=headers, timeout=20.0), attempts=1)
        payload = _exa_payload(response.text)
        if not isinstance(payload, dict):
            raise ValueError("Invalid Exa response")
        error = payload.get("error")
        if error:
            message = str(error.get("message", error)) if isinstance(error, dict) else str(error)
            if "rate limit" in message.lower() or "too many requests" in message.lower():
                raise RetryableError(message)
            raise ValueError(message)
        result = payload.get("result")
        if not isinstance(result, dict):
            raise ValueError("Missing Exa result")
        content = result.get("content", [])
        texts = [item.get("text", "") for item in content if isinstance(item, dict) and item.get("type") == "text"] if isinstance(content, list) else []
        joined = "\n".join(texts).strip()
        if _rate_limited(result) or (result.get("isError") and "rate limit" in joined.lower()):
            raise RetryableError("Exa rate limit")
        if result.get("isError"):
            raise ValueError(joined or "Exa tool error")
        return joined or "NO RESULTS"

    return with_retry(call, attempts=5, cap=60.0)


@tool
def web_search(query: str, objective: str = "", num_results: int = 5) -> str:
    """Search the web (Exa). Describe the ideal page in natural language. Returns clean text of the top results with URLs."""
    try:
        if not query or not query.strip():
            return "NO RESULTS"
        query = query.strip()
        objective = objective.strip() if objective else ""
        return _exa_call("web_search_exa", {"query": query,
                          "objective": objective or f"Find credible sources about {query}",
                          "numResults": _bounded(num_results, 1, 20)})
    except Exception as exc:
        return _error(exc)


@tool
def web_fetch(url: str) -> str:
    """Read the full content of one web page (e.g. an arXiv abstract page) as markdown. Long pages are truncated."""
    try:
        if not url or not url.strip():
            return "NO RESULTS"
        return _exa_call("web_fetch_exa", {"urls": [url.strip()], "maxCharacters": 12000})[:12000]
    except Exception as exc:
        return _error(exc)


SOURCE_TOOLS = [arxiv_search, hf_daily_papers, hf_search_papers, web_search, web_fetch]


if __name__ == "__main__":
    load_dotenv()
    for name, fn, args in [
        ("arxiv_search", arxiv_search, {"query": "world model", "max_results": 3}),
        ("hf_daily_papers", hf_daily_papers, {"limit": 20}),
        ("hf_search_papers", hf_search_papers, {"query": "world model", "limit": 3}),
        ("web_search", web_search, {"query": "survey paper on world models", "num_results": 2}),
        ("web_fetch", web_fetch, {"url": "https://arxiv.org/abs/1803.10122"}),
    ]:
        try:
            print(f"== {name}\n{fn.invoke(args)[:400]}\n")
        except NotImplementedError as exc:
            print(f"== {name}: not implemented yet ({exc})\n")
