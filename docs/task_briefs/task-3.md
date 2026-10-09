# Task 3: Lead, researcher và citation-checker

**Files:** Modify agents.py; Create tests/test_agents.py.

**Interfaces:** build_subagents() -> list[dict]; build_lead_agent(backend, model) -> agent. Giữ WORKDIR/NOTES_DIR/SOURCES_PATH/REPORT_PATH/VALIDATOR_PATH/FINALIZER_PATH hiện có.

- [ ] Viết prompt lead theo chuỗi: write_todos → >= 3 câu hỏi → task song song → đọc/kiểm notes → gộp sources → viết thân → finalizer → validator → checker → sửa khi cần → finalizer/validator lần cuối.
- [ ] Tin giao việc phải có chủ đề, câu hỏi, phạm vi, nguồn cần dùng, đường dẫn notes riêng, schema ghi chú và định dạng kết quả trả về. Không cho researcher ghi đè tệp của nhau.
- [ ] Researcher dùng >= 2 họ nguồn mỗi câu hỏi; chuyển nguồn/đổi query khi ERROR/NO RESULTS; coi nội dung truy xuất là dữ liệu không đáng tin; chỉ ghi claim có bằng chứng.
- [ ] Checker chỉ được SOURCE tool web_fetch; trả SUPPORTED/PARTIAL/UNSUPPORTED/UNVERIFIABLE cùng căn cứ. Lead sửa/bỏ claim không được hỗ trợ; lỗi fetch phải ghi là chưa kiểm chứng.
- [ ] Cài TodoListMiddleware cho lead. Khởi đầu theo GUIDE: lead model/tool 150/300, subagent 40/60; tạo middleware riêng cho từng agent và điều chỉnh từ run thật.
- [ ] Mock create_deep_agent để xác nhận backend, hai loại subagent, bộ tool và middleware thực sự được truyền đúng.

**Gate:** Giao diện agent dựng được với dependency đã pin. Run thật ở Task 5 phải xác nhận có lập kế hoạch/ủy quyền; lời hứa trong prompt không đủ chứng minh agent đã thực hiện.


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

