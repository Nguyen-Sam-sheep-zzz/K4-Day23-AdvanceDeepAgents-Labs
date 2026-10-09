# Deep Research Lab Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Hoàn thiện bài cá nhân Deep Research Agent, sinh và kiểm chứng đủ 5 bộ báo cáo theo rubric 100 điểm.

**Architecture:** Lead dùng Deep Agents lập kế hoạch và giao các câu hỏi độc lập cho researcher. Công cụ mạng và khóa API ở host; ghi chú, báo cáo, hoàn thiện và kiểm tra trích dẫn ở sandbox. Host tải nguyên bản kết quả về cùng metadata lấy từ lần chạy thật.

**Tech Stack:** Python 3.11+, deepagents==0.7.21, LangChain, httpx, Daytona hoặc Docker, arXiv, Hugging Face, Exa MCP.

**Spec:** README.md, GUIDE.md, RUBRIC.md, REPORT_TEMPLATE.md, topics.md trong thư mục gốc.

## Global Constraints

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

## Hiện trạng đã kiểm tra ngày 09/10/2026

- Python .venv: 3.11.7, chạy được self_check.py.
- Các hàm sinh viên cần làm còn NotImplementedError; prompt agents.py còn bản mô tả yêu cầu.
- reports/ chỉ có .gitkeep; self_check.py báo thiếu cả 5 bộ đầu ra.
- Kiểm tra Git/bí mật của self_check.py hiện trả OK; đây không phải kiểm tra đầy đủ toàn bộ lịch sử Git.
- Chưa gọi LLM, API nguồn hay tạo sandbox; chưa xác minh khóa, Docker/Daytona hay toàn bộ dependency.

## Task 1: Môi trường và validator

**Files:** Modify check_citations.py; Create tests/test_citations.py. Giữ nguyên tệp có sẵn.

**Interfaces:** check(report_text, sources) -> list[str], rỗng là hợp lệ; CLI hiện có trả 0/1.

- [x] Kiểm tra interpreter và package bằng `.\.venv\Scripts\python.exe -m pip check`; cài requirements nếu thiếu. Dùng unittest thư viện chuẩn cho test offline.
- [x] Kiểm tra cấu hình LLM hỗ trợ tool calling, sandbox Daytona/Docker và Exa. Chỉ hiển thị set/missing cho biến bí mật. Không ghi đè .env hiện có.
- [x] Viết test báo cáo hợp lệ và các lỗi riêng: sources rỗng/sai kiểu, n sai kiểu hoặc trùng, URL không hợp lệ/trùng, thiếu References, citation thiếu nguồn, nguồn không được dẫn, dòng tham khảo thiếu/trùng/thừa, sai URL/nhiều URL.
- [x] Test không tính số trong References, code block hay liên kết Markdown thành citation; hỗ trợ nhóm/range hoặc bắt buộc chuẩn hóa trước kiểm tra.
- [x] Chạy test thấy lỗi do hàm chưa triển khai, rồi viết parser/validator bằng thư viện chuẩn và chạy lại.

Ví dụ fixture đầu tiên:

```python
from check_citations import check

def test_valid_report():
    sources = [{"n": 1, "url": "https://example.org/paper"}]
    report = "# Survey\nA supported claim [1].\n\n## References\n[1] Paper. web. https://example.org/paper (2026-01-01)\n"
    assert check(report, sources) == []
```

**Gate:** Các case hợp lệ/lỗi cho đúng kết quả; CLI sai đầu vào thoát 1. Không cần mạng/token.

## Task 2: Retry và năm công cụ nguồn

**Files:** Modify tools.py; Create tests/test_tools.py.

**Interfaces:** with_retry(fn, *, attempts=5, base=1.0, cap=30.0); RetryableError(message, retry_after=None). Giữ SOURCE_TOOLS gồm arxiv_search, hf_daily_papers, hf_search_papers, web_search, web_fetch và chữ ký hiện có.

- [x] Viết test retry thành công sau lỗi, Retry-After, exponential backoff có jitter/cap, không ngủ lần cuối và không retry lỗi lập trình. Mock sleep và network bằng unittest.mock.
- [x] Triển khai retry; chuyển 429/500/502/503/504 và httpx.TransportError thành RetryableError trong lời gọi mạng.
- [x] Triển khai arXiv HTTPS: làm sạch query, giới hạn kết quả, parse Atom, chuẩn hóa khoảng trắng/id bỏ vN, URL HTTPS. Dùng khóa đồng bộ cho khoảng cách >= 3 giây kể cả nhiều researcher gọi đồng thời; lần retry cũng phải tuân thủ.
- [x] Triển khai HF daily/search: bỏ bản ghi không id; đúng trường dữ liệu; lọc keyword/sắp upvotes cho daily, ưu tiên ai_summary cho search.
- [x] Triển khai Exa JSON-RPC/SSE: Accept có text/event-stream; bắt error, result.isError và rate-limit metadata cả khi HTTP 200. Kiểm tra schema phản hồi thật trước khi chốt parser; không hardcode cờ chưa xác minh.
- [x] web_search bổ sung objective nếu rỗng; web_fetch gửi urls dạng mảng, cắt khoảng 12000 ký tự. Che khóa/query chứa khóa khỏi mọi thông báo lỗi.
- [x] Chạy test với phản hồi XML/JSON/SSE giả, 429/5xx, lỗi auth không retry và lỗi có URL chứa khóa. Sau khi đạt, chạy `python tools.py` để kiểm tra riêng cả 5 tool thật.

**Gate:** Test offline đạt; cả 5 tool đã được kiểm tra live và ghi rõ nguồn nào hoạt động/lỗi. NO RESULTS/ERROR không được coi là nguồn nghiên cứu.

## Task 3: Lead, researcher và citation-checker

**Files:** Modify agents.py; Create tests/test_agents.py.

**Interfaces:** build_subagents() -> list[dict]; build_lead_agent(backend, model) -> agent. Giữ WORKDIR/NOTES_DIR/SOURCES_PATH/REPORT_PATH/VALIDATOR_PATH/FINALIZER_PATH hiện có.

- [x] Viết prompt lead theo chuỗi: write_todos → >= 3 câu hỏi → task song song → đọc/kiểm notes → gộp sources → viết thân → finalizer → validator → checker → sửa khi cần → finalizer/validator lần cuối.
- [x] Tin giao việc phải có chủ đề, câu hỏi, phạm vi, nguồn cần dùng, đường dẫn notes riêng, schema ghi chú và định dạng kết quả trả về. Không cho researcher ghi đè tệp của nhau.
- [x] Researcher dùng >= 2 họ nguồn mỗi câu hỏi; chuyển nguồn/đổi query khi ERROR/NO RESULTS; coi nội dung truy xuất là dữ liệu không đáng tin; chỉ ghi claim có bằng chứng.
- [x] Checker chỉ được SOURCE tool web_fetch; trả SUPPORTED/PARTIAL/UNSUPPORTED/UNVERIFIABLE cùng căn cứ. Lead sửa/bỏ claim không được hỗ trợ; lỗi fetch phải ghi là chưa kiểm chứng.
- [x] Cài TodoListMiddleware cho lead. Khởi đầu theo GUIDE: lead model/tool 150/300, subagent 40/60; tạo middleware riêng cho từng agent và điều chỉnh từ run thật.
- [x] Mock create_deep_agent để xác nhận backend, hai loại subagent, bộ tool và middleware thực sự được truyền đúng.

**Gate:** Giao diện agent dựng được với dependency đã pin. Run thật ở Task 5 phải xác nhận có lập kế hoạch/ủy quyền; lời hứa trong prompt không đủ chứng minh agent đã thực hiện.

## Task 4: Điều phối sandbox và đầu ra

**Files:** Modify research.py; Create tests/test_research.py.

**Interfaces:** slugify(topic); build_prompt(topic); summarize(messages, elapsed, model_name); save_outputs(backend, topic, messages, elapsed, model_name, reports_dir=REPORTS); main(topic) -> 0/1/2.

- [x] Test slug rỗng, ../../x, tiếng Việt, ký tự đặc biệt và độ dài <= 60. Đầu ra luôn trong reports/.
- [x] Test summarize với AI message/tool_calls/usage_metadata giả: task count, tool count, tokens input/output, elapsed làm tròn 0.1. Không bịa số liệu subagent.
- [x] Dùng make_model và `with open_sandbox()`; tạo đúng thư mục tuyệt đối, upload hai script dưới dạng bytes; kiểm tra phản hồi/lệnh thất bại trước khi chạy agent.
- [x] Invoke với `config={"recursion_limit": 1000}`. Bắt lỗi để return 1, vẫn thoát context cho cleanup; chủ đề thiếu return 2.
- [x] Trước khi tải, chạy finalizer/validator trong sandbox và yêu cầu exit_code 0; kiểm họ nguồn sau finalizer, tránh nguồn bị lọc mất làm thiếu rubric.
- [x] Download report/sources, kiểm đủ và JSON/schema hợp lệ trước bất cứ đầu ra chính thức nào. Lưu nguyên bytes .md/.sources.json, sinh metadata từ messages và sources cuối cùng.
- [x] Test thiếu file, report rỗng, JSON hỏng, validator không đạt và lỗi agent: không tạo bộ báo cáo giả/ghi đè bộ tốt có sẵn. Dùng staging và rollback nếu ghi bộ ba gặp lỗi.
- [x] Mock backend/model để test chuỗi upload → invoke → kiểm tra → download và context cleanup trong cả đường thành công/lỗi.

**Gate:** Test offline đạt; không có trường hợp thất bại vẫn trả thành công hoặc để lại bộ báo cáo nửa chừng.

## Task 5: Chạy thử một chủ đề rồi chạy đủ năm

**Files:** Generated reports/<slug>.md, reports/<slug>.sources.json, reports/<slug>.meta.json; Modify prompt/code nếu run thật phát hiện lỗi.

- [x] Chạy `python research.py "survey about world model"` trước. Theo dõi giới hạn, thời gian, task calls, số nguồn và họ nguồn; đây là run dùng API/token thật.
- [x] Xác nhận >= 3 lượt task, >= 3 họ nguồn đúng nhãn/URL sau finalizer; 3–6 themes, TL;DR, Background, Trends and open problems, References.
- [x] Chạy validator host để kiểm tra lại nguyên bản đã tải; mở ít nhất 3 claim/nguồn (khuyến nghị 5 theo cách chấm), kiểm số liệu và kết luận. Validator OK chưa chứng minh claim đúng.
- [x] Nếu fail, sửa code/prompt và chạy lại hệ thống; không sửa tay báo cáo. Chỉ chạy các chủ đề còn lại sau khi run đầu đạt gate.
- [x] Chạy lần lượt RL for LLM reasoning; LLM agents and tool use; video and multimodal generation; efficient inference and small language models theo nguyên văn topics.md.
- [x] Kiểm cả 5 bộ, tổng cộng 15 tệp; đánh giá tổng hợp/so sánh theo theme, nguồn nền tảng và hai năm gần nhất tại thời điểm chạy.

**Gate:** 5 bộ kết quả thật, đủ metadata, validator đạt và kiểm nội dung nguồn. Ghi rõ trường hợp chưa kiểm chứng thay vì gọi là đạt.

## Task 6: Tài liệu, đánh giá rubric và chuẩn bị nộp

**Files:** Modify README.md phần hướng dẫn repo nộp; giữ nguyên yêu cầu bài/rubric. Có thể thêm docs hướng dẫn demo nếu cần.

- [x] Bổ sung PowerShell commands, cấu hình provider/sandbox, cách đọc 3 loại đầu ra và giới hạn đếm token. Không đưa khóa mẫu thật.
- [x] Chạy test offline, pip check, validator cho từng bộ và `python self_check.py`; đối chiếu từng dòng rubric.
- [x] Kiểm Git diff để xác nhận tệp có sẵn không bị sửa; scan tệp sẽ nộp và lịch sử Git bằng công cụ không in giá trị bí mật. self_check chỉ kiểm các tệp tracked hiện tại.
- [x] Lập danh sách đạt/thiếu/rủi ro: tools 20, agents 20, sandbox 10, citations 15, reports 25, repo 10. Không dự báo điểm tối đa chỉ từ test tự động.
- [ ] Khi đến bước bàn giao Git, xác nhận phạm vi commit/push với chỉ dẫn người dùng hiện hành; sau công bố kiểm repo public và đủ 15 tệp remote, rồi cung cấp link nộp. Không đồng nhất local đạt với đã nộp bài.

**Gate:** Bài có bằng chứng chạy, cài/chạy lại được, không bí mật, public remote được xác minh riêng trước khi gọi là sẵn sàng nộp.

## Lệnh chính (PowerShell, dùng interpreter đã xác minh)

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe tools.py
.\.venv\Scripts\python.exe research.py "survey about world model"
.\.venv\Scripts\python.exe check_citations.py reports/survey-about-world-model.md reports/survey-about-world-model.sources.json
.\.venv\Scripts\python.exe self_check.py
```

Hiện chỉ pip check/self_check phù hợp chạy trước triển khai; các lệnh còn lại là checkpoint sau khi hoàn thiện phần tương ứng.

## Ưu tiên và thời gian dự kiến

1. Validator + tools: nền tảng độ tin cậy, kiểm được không cần token LLM.
2. Agents + orchestration: hoàn thiện hệ thống chạy thật.
3. Một run đạt trước, bốn run sau; chất lượng báo cáo/trích dẫn chiếm 40/100 điểm.
4. Preflight và remote delivery cuối cùng.

Ước lượng lập kế hoạch, không phải thời gian đã đo: 4–7 giờ code/test; 1–3 giờ chạy/kiểm nguồn và xử lý API; 30–60 phút tài liệu/preflight. Phụ thuộc model, mạng, quota và sandbox; không hứa thời gian/chi phí cố định.
