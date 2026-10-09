# Task 6: Tài liệu, đánh giá rubric và chuẩn bị nộp

**Files:** Modify README.md phần hướng dẫn repo nộp; giữ nguyên yêu cầu bài/rubric. Có thể thêm docs hướng dẫn demo nếu cần.

- [ ] Bổ sung PowerShell commands, cấu hình provider/sandbox, cách đọc 3 loại đầu ra và giới hạn đếm token. Không đưa khóa mẫu thật.
- [ ] Chạy test offline, pip check, validator cho từng bộ và `python self_check.py`; đối chiếu từng dòng rubric.
- [ ] Kiểm Git diff để xác nhận tệp có sẵn không bị sửa; scan tệp sẽ nộp và lịch sử Git bằng công cụ không in giá trị bí mật. self_check chỉ kiểm các tệp tracked hiện tại.
- [ ] Lập danh sách đạt/thiếu/rủi ro: tools 20, agents 20, sandbox 10, citations 15, reports 25, repo 10. Không dự báo điểm tối đa chỉ từ test tự động.
- [ ] Khi đến bước bàn giao Git, xác nhận phạm vi commit/push với chỉ dẫn người dùng hiện hành; sau công bố kiểm repo public và đủ 15 tệp remote, rồi cung cấp link nộp. Không đồng nhất local đạt với đã nộp bài.

**Gate:** Bài có bằng chứng chạy, cài/chạy lại được, không bí mật, public remote được xác minh riêng trước khi gọi là sẵn sàng nộp.


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

