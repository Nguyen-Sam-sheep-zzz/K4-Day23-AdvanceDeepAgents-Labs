# Task 4: Điều phối sandbox và đầu ra

**Files:** Modify research.py; Create tests/test_research.py.

**Interfaces:** slugify(topic); build_prompt(topic); summarize(messages, elapsed, model_name); save_outputs(backend, topic, messages, elapsed, model_name, reports_dir=REPORTS); main(topic) -> 0/1/2.

- [ ] Test slug rỗng, ../../x, tiếng Việt, ký tự đặc biệt và độ dài <= 60. Đầu ra luôn trong reports/.
- [ ] Test summarize với AI message/tool_calls/usage_metadata giả: task count, tool count, tokens input/output, elapsed làm tròn 0.1. Không bịa số liệu subagent.
- [ ] Dùng make_model và `with open_sandbox()`; tạo đúng thư mục tuyệt đối, upload hai script dưới dạng bytes; kiểm tra phản hồi/lệnh thất bại trước khi chạy agent.
- [ ] Invoke với `config={"recursion_limit": 1000}`. Bắt lỗi để return 1, vẫn thoát context cho cleanup; chủ đề thiếu return 2.
- [ ] Trước khi tải, chạy finalizer/validator trong sandbox và yêu cầu exit_code 0; kiểm họ nguồn sau finalizer, tránh nguồn bị lọc mất làm thiếu rubric.
- [ ] Download report/sources, kiểm đủ và JSON/schema hợp lệ trước bất cứ đầu ra chính thức nào. Lưu nguyên bytes .md/.sources.json, sinh metadata từ messages và sources cuối cùng.
- [ ] Test thiếu file, report rỗng, JSON hỏng, validator không đạt và lỗi agent: không tạo bộ báo cáo giả/ghi đè bộ tốt có sẵn. Dùng staging và rollback nếu ghi bộ ba gặp lỗi.
- [ ] Mock backend/model để test chuỗi upload → invoke → kiểm tra → download và context cleanup trong cả đường thành công/lỗi.

**Gate:** Test offline đạt; không có trường hợp thất bại vẫn trả thành công hoặc để lại bộ báo cáo nửa chừng.


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

