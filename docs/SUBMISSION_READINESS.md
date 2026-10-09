# Kiểm tra nộp bài — 09/10/2026

**Phần local đã hoàn thiện và kiểm tra. Chưa commit/push, chưa đưa các báo cáo lên GitHub.** Nhánh hiện tại: `feature/deep-research-lab`; nhánh gốc `main` ở commit `48a1223`. Repo GitHub là public, nhưng `main` remote hiện có **0/15** tệp báo cáo cần nộp. Trạng thái này phải được kiểm lại sau khi công bố.

## Kết quả thật

Model: `gpt-6-luna`, endpoint tương thích do người dùng cấu hình. Sandbox: Docker. Báo cáo/nguồn do agent viết và hoàn thiện trong sandbox rồi tải nguyên bytes về; không sửa nội dung trên host.

| Chủ đề | Nguồn | Số tag | Researcher thành công | Checker thành công | Batch researcher |
|---|---:|---:|---:|---:|---:|
| World model | 14 | 4 | 4 | 1 | 3 |
| RL for LLM reasoning | 12 | 4 | 3 | 1 | 3 |
| LLM agents and tool use | 11 | 4 | 3 | 1 | 3 |
| Video and multimodal generation | 12 | 4 | 4 | 1 | 3 |
| Efficient inference and small language models | 18 | 3 | 4 | 1 | 3 |

Đủ **15 tệp** `.md`, `.sources.json`, `.meta.json` trong `reports/`. Cả năm bộ đạt validator và `self_check.py`. Bộ test offline đạt **72/72**; `pip check` sạch; `git diff --check` sạch. Năm công cụ đã trả dữ liệu thật trong lần chạy `tools.py` cuối; arXiv 429 ở các lần trước đã được ghi lại, không giấu lỗi.

Kiểm nguồn độc lập đã mở lại ít nhất sáu URL mỗi báo cáo và đối chiếu 6–7 claim mỗi chủ đề (32 claim trong năm bản cuối). Đây là kiểm mẫu, không tái hiện thí nghiệm của các paper. Chi tiết: [CLAIM_AUDIT.md](evidence/CLAIM_AUDIT.md). Hash của 15 tệp, metadata, hash tệp cấp sẵn và cleanup: [final_preflight.json](evidence/final_preflight.json).

## Đối chiếu từng dòng rubric

| Tiêu chí | Bằng chứng / trạng thái |
|---|---|
| 1.1 Retry | Backoff, jitter, Retry-After/cap, số lần thử hữu hạn, không ngủ cuối; test lỗi retry/nonretry đạt. |
| 1.2 Năm tool | Parser/dạng record, NO RESULTS/ERROR, che bí mật; test và live smoke của cả năm đạt. |
| 1.3 Exa | JSON/SSE/JSON-RPC, rate limit HTTP200, retry và che khóa; test/live đạt. |
| 1.4 arXiv | HTTPS, chuẩn hóa query/ID, khóa đồng bộ khoảng cách ≥3 giây gồm retry; test/live đạt. |
| 2.1 Uỷ quyền | Mỗi meta có ≥3 task request và ≥3 researcher thực sự trả thành công. |
| 2.2 Đa nguồn | Mỗi bộ có 3–4 tag thật; URL/ID được đối chiếu. Web lấy URL arXiv vẫn mang tag web. |
| 2.3 Lead | Todo, batch 3 researcher, đủ ngữ cảnh, đọc notes, merge, finalize, validate, checker; metadata và notes thật. |
| 2.4 Researcher | Prompt cấm làm theo nội dung web, không lấy số liệu từ trí nhớ; notes có excerpt, provenance và gaps. |
| 2.5 Giới hạn | Lead 150 model/300 tool mỗi invocation; subagent 40/60; recursion 1000; CLI tối đa 1 lượt sửa output. |
| 3.1 Sandbox thật | Upload hai script, agent execute, notes/report/sources trong Docker rồi download; live runs và tests đạt. |
| 3.2 Cleanup/bí mật | open_sandbox cleanup cả khi lỗi; không upload .env; gate lỗi không xuất trio rỗng/ghi đè bản tốt. Không còn container lab. |
| 4.1 Validator | Cả 5 bộ OK; kiểm parse/exclusion/duplicate/References bằng tests. Giảng viên dùng validator riêng. |
| 4.2 Kiểm mẫu nguồn | 32 claim đối chiếu với nguồn trong bản cuối; kết luận hỗ trợ có giới hạn phạm vi, không tuyên bố kiểm hết báo cáo. |
| 5.1 Cấu trúc | Tiêu đề bắt buộc đúng chữ, 3–5 TL;DR bullets có citation, 3–6 themes, References cuối. |
| 5.2 Tổng hợp | So sánh phương pháp, mục tiêu và chế độ đánh giá theo theme; World Model đã tái sinh để giảm lặp. Chấm thủ công. |
| 5.3 Chính xác/cụ thể | Số liệu mẫu đã kiểm; câu dẫn sai paper trong video đã được giải quyết bằng system rerun; số liệu chưa kiểm được bị loại. Chấm thủ công. |
| 5.4 Nguồn nền tảng/gần đây | Các bản cuối có primary foundational context và nguồn 2024–2026; một số ngày là version/indexing, một số web records không rõ ngày. |
| 5.5 Xu hướng/vấn đề mở | Mỗi báo cáo có mục riêng, nêu giới hạn và tránh xếp hạng giữa benchmark khác protocol. Chấm thủ công. |
| 6.1 Bí mật | .env bị ignore; scan cả tracked/untracked candidate, KEY_LIKE và giá trị secret hiện cấu hình; lịch sử Git không có match. |
| 6.2 README | Có setup PowerShell, provider/Docker, lệnh chạy/kiểm và cách đọc metadata/giới hạn token. |
| 6.3 Mã sạch/tệp cấp sẵn | Review đạt, tests đạt; tám tệp được bảo vệ vẫn nguyên SHA256, gồm model/sandbox/finalizer/self-check và đề. |
| 6.4 Requirements | Pin có sẵn được giữ nguyên; môi trường Python 3.11.7 dùng được, pip check sạch. |

## Giới hạn cần hiểu khi nộp

- HF-generated summaries được báo cáo ghi rõ; chúng không thay thế primary-paper verification cho mọi chi tiết. Số liệu paper là kết quả tác giả báo cáo, không phải phép đo lại của lab này.
- `tokens` chỉ tính tin nhắn lead, không gồm subagent hay các lượt chạy bị loại. Không dùng nó để tuyên bố tổng token/chi phí hệ thống.
- Validator và self-check kiểm phần tự động. Chất lượng tổng hợp, tính đầy đủ và độ đúng của các claim ngoài mẫu vẫn do người chấm đánh giá; không suy ra điểm 100 từ tests.
- Các bản cũ lỗi/đã thay thế được giữ trong `docs/evidence/` với nhãn rõ. Bộ nộp hiện hành chỉ là năm trio trong `reports/`.

## Kiểm lại trước công bố

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -q
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe self_check.py
git diff --check
git status --short
```

Sau commit/push, kiểm GitHub có đủ 15 tệp đúng hash trên nhánh nộp và repo vẫn public. Link repo: https://github.com/Nguyen-Sam-sheep-zzz/K4-Day23-AdvanceDeepAgents-Labs
