# Task 2: Retry và năm công cụ nguồn

**Files:** Modify tools.py; Create tests/test_tools.py.

**Interfaces:** with_retry(fn, *, attempts=5, base=1.0, cap=30.0); RetryableError(message, retry_after=None). Giữ SOURCE_TOOLS gồm arxiv_search, hf_daily_papers, hf_search_papers, web_search, web_fetch và chữ ký hiện có.

- [ ] Viết test retry thành công sau lỗi, Retry-After, exponential backoff có jitter/cap, không ngủ lần cuối và không retry lỗi lập trình. Mock sleep và network bằng unittest.mock.
- [ ] Triển khai retry; chuyển 429/500/502/503/504 và httpx.TransportError thành RetryableError trong lời gọi mạng.
- [ ] Triển khai arXiv HTTPS: làm sạch query, giới hạn kết quả, parse Atom, chuẩn hóa khoảng trắng/id bỏ vN, URL HTTPS. Dùng khóa đồng bộ cho khoảng cách >= 3 giây kể cả nhiều researcher gọi đồng thời; lần retry cũng phải tuân thủ.
- [ ] Triển khai HF daily/search: bỏ bản ghi không id; đúng trường dữ liệu; lọc keyword/sắp upvotes cho daily, ưu tiên ai_summary cho search.
- [ ] Triển khai Exa JSON-RPC/SSE: Accept có text/event-stream; bắt error, result.isError và rate-limit metadata cả khi HTTP 200. Kiểm tra schema phản hồi thật trước khi chốt parser; không hardcode cờ chưa xác minh.
- [ ] web_search bổ sung objective nếu rỗng; web_fetch gửi urls dạng mảng, cắt khoảng 12000 ký tự. Che khóa/query chứa khóa khỏi mọi thông báo lỗi.
- [ ] Chạy test với phản hồi XML/JSON/SSE giả, 429/5xx, lỗi auth không retry và lỗi có URL chứa khóa. Sau khi đạt, chạy `python tools.py` để kiểm tra riêng cả 5 tool thật.

**Gate:** Test offline đạt; cả 5 tool đã được kiểm tra live và ghi rõ nguồn nào hoạt động/lỗi. NO RESULTS/ERROR không được coi là nguồn nghiên cứu.


## Global constraints

- Bài thực hành cá nhân; đầu ra nộp là public GitHub repo có mã và reports/.
- Giữ nguyên model.py, sandbox.py, self_check.py, finalize_citations.py và dữ liệu đề/rubric.
- Triển khai 4 tệp: check_citations.py, tools.py, agents.py, research.py; thêm test và hướng dẫn chạy khi cần.
- Không đưa .env hoặc bí mật vào sandbox, log, báo cáo hay Git.
- Tool trả chuỗi: dữ liệu, NO RESULTS hoặc ERROR: ...; không để ngoại lệ thoát ra agent.
- Tất cả bước sửa trích dẫn chạy trong sandbox trước khi validator in OK. Không sửa tay báo cáo, không viết lại báo cáo/nguồn sau download.
- Báo cáo tiếng Anh đúng REPORT_TEMPLATE.md, có 3–6 phần theo chủ đề.
- Mỗi chủ đề có .md, .sources.json, .meta.json; metadata thật có subagent_calls >= 3 và ít nhất 3 giá trị source hợp lệ.
- source là công cụ đã lấy nguồn, thuộc arxiv, hf-daily, hf-search, web. Ưu tiên phối hợp arXiv + Hugging Face + web để có đa dạng thực chất.
- Giới hạn model/tool cho lead và từng subagent; đặt recursion_limit rõ ràng.
- Không tự suy ra chi phí toàn hệ thống từ tokens của lead.

