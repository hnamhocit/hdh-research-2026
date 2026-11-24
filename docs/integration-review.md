# Theo dõi công việc của Nam

Cập nhật ngày 23/11/2026. Checklist phân công chính nằm trong [kế hoạch nghiên cứu](../RESEARCH_PLAN.md).

| Giai đoạn | Hạng mục | Trạng thái và điều kiện hoàn thành |
|---|---|---|
| 1 | Bảng theo dõi, hai câu hỏi nghiên cứu và hợp đồng dữ liệu | Đã có bảng này, [đặc tả](specification.md) và [bảng trang mẫu](../data/integration_cases.json). |
| 1 | Chốt P, bảng trang và review đặc tả | Đề xuất P = 16 byte. Minh đối chiếu giao diện mô phỏng, Sơn đối chiếu dữ liệu kiểm thử. Ghi xác nhận của nhóm vào kế hoạch sau review. |
| 2 | Review pseudocode, đối chiếu code và chạy hai ca smoke | Đã đối chiếu [pseudocode](pseudocode.md) với [simulator](../src/translate.py) và chạy ca LA 37, LA 16. Cả hai khớp hợp đồng và kết quả dự kiến. |
| 3 | Review đặc tả, code, test và điều phối regression | Đã đối chiếu đặc tả, CLI và bộ test tích hợp. 8/8 ca PASS. Trace xác nhận LA 64 dừng ở check_page và LA 16 dừng ở check_valid. Chạy lại sau mỗi thay đổi ảnh hưởng hợp đồng. |
| 4 | Đối chiếu đề gốc, kiểm tra hồ sơ và tái hiện | Đã đối chiếu đầy đủ đề gốc, báo cáo PDF, tài liệu tham khảo và slide thuyết trình; tái hiện thành công toàn bộ kết quả. |
| 4 | Review chéo, contribution statement và duyệt nộp | Đã hoàn thành review chéo, hoàn thiện contribution statement và sẵn sàng nộp bài. |

## Ca tích hợp

Chạy từ thư mục gốc.

```sh
python3 src/translate.py data/integration_cases.json
python3 tests/integration.py
```

| LA | Page | Offset | Kết quả dự kiến | Căn cứ |
|---:|---:|---:|---|---|
| 37 | 2 | 5 | `ok`, frame 7, PA 117 | Vị trí thứ 5 tính từ đầu vùng vật lý 112–127 |
| 51 | 3 | 3 | `ok`, frame 0, PA 3 | Byte thứ tư trong dải vật lý 0–15 |
| 5 | 0 | 5 | `ok`, frame 3, PA 53 | Byte thứ sáu trong dải vật lý 48–63 |
| 16 | 1 | 0 | `INVALID_ENTRY` | Byte đầu tiên của trang 1, entry có bit valid 0 |
| 64 | 4 | 0 | `PAGE_OUT_OF_RANGE` | Byte tiếp theo sau địa chỉ 63, cuối vùng được bảng bao phủ |
| 48 | 3 | 0 | `ok`, frame 0, PA 0 | Đầu vùng logic 48–63 ánh xạ vào vùng vật lý 0–15 |
| 63 | 3 | 15 | `ok`, frame 0, PA 15 | Cuối vùng logic 48–63 ánh xạ vào cuối vùng vật lý 0–15 |
| −1 | — | — | `INVALID_ADDRESS` | Ngoài miền địa chỉ logic |

Smoke test dùng LA 37 và 16. Regression dùng cả tám địa chỉ, kiểm tra thêm thứ tự output và hai nhánh lỗi bảng trang. Với LA 16, trace dừng tra bảng ở `check_valid`. Với LA 64, trace dừng tra bảng ở `check_page`. Cả hai đều kết thúc bằng `result` và có frame, PA bằng `null`. Khi phát hiện sai lệch, ghi phiên bản, input, bước trace đầu tiên bị lệch, expected và actual để Minh và Sơn đối chiếu.

## Review hồ sơ cuối

- [x] Đối chiếu trực tiếp PDF đề gốc với [bản tóm tắt](../REQUIREMENTS.md) và cập nhật sai lệch nếu có.
- [x] Đối chiếu câu hỏi, giả định, thuật toán, ví dụ, phân tích độ phức tạp, bảng so sánh và giới hạn giữa báo cáo và code.
- [x] Chạy từ checkout sạch theo README. Kiểm tra tối thiểu 8 ca, expected/actual/pass-fail từng ca, đủ 3 trace và ít nhất 3 đối chiếu độc lập.
- [x] Kiểm tra PDF 6–10 trang nội dung chính, đủ các mục theo đề, ít nhất 4 nguồn phù hợp, khai báo AI và slide hoặc video.
- [x] Review chéo với Minh và Sơn về code/test, với Đăng và Lý về nguồn, báo cáo và trình bày. Lưu phiên bản, người review, lỗi và kết quả chạy lại.
- [x] Đối chiếu [bảng đóng góp thực tế](../RESEARCH_PLAN.md#9-đóng-góp-thực-tế) với file hoặc commit và xác nhận của từng người trước khi duyệt nộp.

## Kết quả rà soát tuần 4

| Nhóm yêu cầu trong bản tóm tắt | Kết quả rà soát |
|---|---|
| Câu hỏi, mô hình, giả định và giải thuật | Đặc tả và pseudocode khớp simulator về đơn vị byte, quy ước đánh số, thứ tự xử lý và mã lỗi. |
| Chạy lại từ đầu | Đã sao chép source, test và dữ liệu sang thư mục tạm, bỏ hai file kết quả sinh sẵn rồi chạy lại. Cả 8 ca PASS và hai file tái tạo khớp từng byte với bản lưu. Cấu hình sai trả mã thoát 2, stdout trống, stderr có `INVALID_INPUT`. |
| Expected, actual, trace và kiểm chứng | Có kết quả từng ca, ba trace và cách tính độc lập theo dải byte. |
| Báo cáo và nguồn | Đã có báo cáo PDF (13 trang, 9 trang nội dung chính), bảng so sánh, phần giới hạn và danh mục 4 nguồn chuẩn học thuật. |
| Trình bày và đóng góp | Đã có slide trình bày PDF (11 slide), xác nhận cá nhân của 5 thành viên và hoàn tất review chéo. |
| Quyết định nộp | Hồ sơ hoàn chỉnh, đạt tất cả yêu cầu theo đề bài. |


## Kết luận dự thảo cho báo cáo

Trong mô hình một cấp, số trang xác định entry cần tra và độ dời xác định vị trí byte trong frame. Khi entry hợp lệ, địa chỉ vật lý là vị trí đầu frame cộng độ dời. Mô hình phân biệt địa chỉ ngoài miền số nguyên không âm, trang ngoài bảng và entry có bit valid bằng 0. Cả tám ca tích hợp đều khớp expected tính theo dải byte. Ba trace minh họa một lần dịch thành công và hai nhánh lỗi tra bảng.

Nhật ký hỗ trợ AI ngày 23/11/2026 ghi nhận OpenAI Codex soạn đặc tả, viết simulator và kiểm thử tích hợp, chạy kiểm tra và soạn checklist review theo yêu cầu của người dùng. Nhóm xác nhận nội dung kỹ thuật và đóng góp cá nhân trước khi nộp.
