"""Reopen selected report sources without changing submitted artifacts."""
import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from tools import _redact, web_fetch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stem", help="Report filename stem in reports/")
    parser.add_argument("numbers", nargs="+", type=int)
    args = parser.parse_args()
    if Path(args.stem).name != args.stem or not args.stem:
        parser.error("stem must be a filename without directories")
    load_dotenv(ROOT / ".env")
    report = ROOT / "reports" / f"{args.stem}.md"
    source_path = ROOT / "reports" / f"{args.stem}.sources.json"
    original = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in (report, source_path)}
    sources = json.loads(source_path.read_text(encoding="utf-8"))
    indexed = {source["n"]: source for source in sources}
    if any(n not in indexed for n in args.numbers):
        parser.error("citation number is absent from sources")
    output = ROOT / "docs" / "evidence" / args.stem / "source-fetches"
    output.mkdir(parents=True, exist_ok=True)

    def fetch(number):
        source = indexed[number]
        content = _redact(web_fetch.invoke({"url": source["url"]}))
        (output / f"{number:02d}.txt").write_text(content, encoding="utf-8")
        return {"n": number, "url": source["url"], "chars": len(content),
                "status": "error" if content.startswith(("ERROR:", "NO RESULTS")) else "retrieved"}

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, dict.fromkeys(args.numbers)))
    (output / "fetch_index.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    if any(hashlib.sha256(p.read_bytes()).hexdigest() != digest for p, digest in original.items()):
        raise RuntimeError("Report or sources changed during read-only audit")
    print(json.dumps(results, indent=2))
    return int(any(result["status"] == "error" for result in results))


if __name__ == "__main__":
    sys.exit(main())
