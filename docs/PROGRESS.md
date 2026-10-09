# Tiến độ triển khai — 09/10/2026

Kế hoạch: [deep-research-lab.md](superpowers/plans/2026-10-09-deep-research-lab.md). Người dùng đã duyệt làm từng bước và chọn `gpt-6-luna`.

| Bước | Trạng thái cuối |
|---|---|
| 1. Môi trường và validator | Hoàn tất: Python 3.11.7, dependency, Docker, validator/CLI. |
| 2. Retry và nguồn | Hoàn tất: 5 công cụ đã trả dữ liệu thật trong live smoke cuối. |
| 3. Agents | Hoàn tất: Todo, ngữ cảnh đầy đủ, batch 3 researcher, checker và giới hạn riêng. |
| 4. Runner | Hoàn tất: sandbox, nguyên bytes, gate/rollback, task-result matching, 1 output repair và feedback CLI. |
| 5. Báo cáo | Hoàn tất: 5 bộ/15 tệp, validator OK, 32 claim kiểm mẫu độc lập. |
| 6. Chuẩn bị nộp | Phần local hoàn tất; commit/push và xác minh tệp remote chờ lựa chọn của người dùng. |

Kiểm cuối: **72/72 tests**, pip check, self-check và diff check đạt. Tám tệp cấp sẵn nguyên SHA256. Scan cả tệp candidate chưa tracked và lịch sử Git không tìm thấy pattern/giá trị secret đang cấu hình. Không còn container lab.

Nhánh local `feature/deep-research-lab`; chưa commit/push. Repo public được xác minh lại, nhưng `main` remote vẫn có 0/15 tệp báo cáo. Không đồng nhất local đạt với đã công bố/nộp.

Chi tiết: [SUBMISSION_READINESS.md](SUBMISSION_READINESS.md), [CLAIM_AUDIT.md](evidence/CLAIM_AUDIT.md), [final_preflight.json](evidence/final_preflight.json), [implementation_status.json](implementation_status.json).

## Các lỗi thật và cách xử lý

- Model từng trả 401/Invalid token; người dùng cập nhật `.env`, các run cuối thành công. Không đưa khóa vào repo/sandbox.
- Docker từng crash với Access denied. Đã phục hồi bằng chờ tiến trình tắt và giữ backup thư mục IPC rỗng; không reset image/container data.
- arXiv từng trả 429; tool xử lý lỗi/retry có giới hạn. Live smoke cuối đã trả dữ liệu.
- World Model attempt1 thiếu tag sau finalizer nên bị từ chối; attempt2 giao việc tuần tự nên dừng. Middleware yêu cầu batch thật và metadata phân biệt request với successful result.
- Video attempt1 sai chữ hoa tiêu đề nên không xuất; attempt2 đạt cấu trúc nhưng có hai claim dẫn sai paper. Kiểm nguồn độc lập từ chối bản đó; attempt3 sinh lại bằng phản hồi reviewer, checker đọc toàn Background và số liệu. Bản cuối dẫn đúng VideoGPT/DreamFoley và bỏ duration limit chưa kiểm được.
- World Model attempt4 tái sinh với nguồn nền tảng gốc và giảm lặp; thay thế attempt3 bằng runner, không sửa tay báo cáo.

Các bản bị loại/đã thay thế chỉ nằm dưới `docs/evidence/`, có nhãn rõ. Bộ hiện hành để nộp là năm trio trong `reports/`.
