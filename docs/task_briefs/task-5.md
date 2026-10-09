# Task 5: Chạy thử một chủ đề rồi chạy đủ năm

**Files:** Generated reports/<slug>.md, reports/<slug>.sources.json, reports/<slug>.meta.json; Modify prompt/code nếu run thật phát hiện lỗi.

- [ ] Chạy `python research.py "survey about world model"` trước. Theo dõi giới hạn, thời gian, task calls, số nguồn và họ nguồn; đây là run dùng API/token thật.
- [ ] Xác nhận >= 3 lượt task, >= 3 họ nguồn đúng nhãn/URL sau finalizer; 3–6 themes, TL;DR, Background, Trends and open problems, References.
- [ ] Chạy validator host để kiểm tra lại nguyên bản đã tải; mở ít nhất 3 claim/nguồn (khuyến nghị 5 theo cách chấm), kiểm số liệu và kết luận. Validator OK chưa chứng minh claim đúng.
- [ ] Nếu fail, sửa code/prompt và chạy lại hệ thống; không sửa tay báo cáo. Chỉ chạy các chủ đề còn lại sau khi run đầu đạt gate.
- [ ] Chạy lần lượt RL for LLM reasoning; LLM agents and tool use; video and multimodal generation; efficient inference and small language models theo nguyên văn topics.md.
- [ ] Kiểm cả 5 bộ, tổng cộng 15 tệp; đánh giá tổng hợp/so sánh theo theme, nguồn nền tảng và hai năm gần nhất tại thời điểm chạy.

**Gate:** 5 bộ kết quả thật, đủ metadata, validator đạt và kiểm nội dung nguồn. Ghi rõ trường hợp chưa kiểm chứng thay vì gọi là đạt.


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

