# Đặc tả dịch địa chỉ bằng bảng trang một cấp

Bản kỹ thuật dùng để triển khai và kiểm thử, dựa trên [bản tóm tắt yêu cầu](../REQUIREMENTS.md). Minh và Sơn cần xác nhận hợp đồng trước khi nhóm chốt.

## Câu hỏi nghiên cứu

1. **Bảng trang một cấp dịch LA sang PA thế nào?** Tách địa chỉ logic thành số trang và độ dời. Dùng số trang để tra trực tiếp một entry. Với entry hợp lệ, thay số trang bằng số frame và giữ nguyên độ dời.
2. **Khi nào địa chỉ không hợp lệ?** Địa chỉ ngoài miền số nguyên không âm bị từ chối. Với địa chỉ trong miền đó, phép dịch lỗi nếu số trang vượt phạm vi bảng hoặc entry tại vị trí đó có bit valid bằng 0.

## Phạm vi và giả định

- Mô phỏng một không gian địa chỉ, một bảng trang một cấp và một kích thước trang cố định trong mỗi lần chạy. Trang và frame cùng kích thước. Mọi địa chỉ, kích thước và độ dời tính theo byte.
- Page và frame đánh số từ 0. Với bảng có N entry, chỉ số trang trong bảng là 0 đến N − 1. N có thể bằng 0. Frame hợp lệ là số nguyên không âm. Mô hình không đặt giới hạn trên cho frame hay LA và cho phép nhiều trang trỏ vào cùng frame.
- Dùng số nguyên chính xác. Bit valid biểu diễn bằng số nguyên 0 hoặc 1. Giá trị boolean, chuỗi và số thực không được coi là số nguyên.
- TLB, bảng trang nhiều cấp, cấp phát frame, thay trang, working set, thrashing, driver và GUI nằm ngoài phạm vi.

## Dữ liệu và giao diện

Lệnh tích hợp dự kiến là `python3 src/translate.py INPUT.json`. Một file JSON có hai trường bắt buộc `page_size` và `page_table`, cùng trường bắt buộc `addresses` là mảng địa chỉ cần dịch theo thứ tự. Xem [file mẫu](../data/integration_cases.json).

| Trường | Kiểu và ràng buộc |
|---|---|
| `page_size` | Số nguyên dương. Bộ dữ liệu chung dùng 16 byte. |
| `page_table` | Mảng entry. Chỉ số trong mảng là số trang. |
| `page_table[i]` | Object có `valid` và `frame`. Với `valid=1`, frame là số nguyên không âm. Với `valid=0`, frame là `null`. |
| `addresses[i]` | LA tính bằng byte. Kiểu hoặc giá trị sai sinh lỗi riêng cho địa chỉ đó. |

Khi cấu hình hợp lệ, stdout là một mảng JSON theo thứ tự đầu vào và mã thoát là 0, kể cả khi một số địa chỉ dịch lỗi. Mỗi phần tử có các trường sau.

| Trường | Giá trị |
|---|---|
| `logical_address` | Giá trị JSON đầu vào |
| `status` | `ok` hoặc `error` |
| `page`, `offset` | Số nguyên sau khi tách địa chỉ hoặc `null` nếu LA sai |
| `frame`, `physical_address` | Số nguyên khi dịch thành công, `null` khi lỗi |
| `error` | `null` khi thành công hoặc mã lỗi dịch bên dưới |
| `trace` | Mảng object có `step` và các giá trị ghi nhận ở bước đó |

Nếu file không đọc được, JSON sai hoặc cấu hình sai kiểu/ràng buộc, ghi chẩn đoán `INVALID_INPUT` vào stderr, để stdout trống và thoát với mã 2. Kiểm tra toàn bộ cấu hình trước khi dịch. Mảng địa chỉ rỗng trả `[]`.

## Thứ tự xử lý và trace

| Bước | Xử lý | Dữ liệu cần ghi trong trace |
|---|---|---|
| 1. `validate_address` | Kiểm tra LA là số nguyên không âm. Dừng với `INVALID_ADDRESS` nếu sai. | `logical_address`, `passed` |
| 2. `split` | Tính `page = LA // P` và `offset = LA % P`. | `page_size`, `page`, `offset` |
| 3. `check_page` | Kiểm tra `page < N`. Dừng với `PAGE_OUT_OF_RANGE` nếu sai. | `page`, `page_count`, `passed` |
| 4. `check_valid` | Đọc bit valid. Dừng với `INVALID_ENTRY` nếu bit bằng 0. | `page`, `valid` |
| 5. `read_frame` | Lấy frame từ entry. | `frame` |
| 6. `compute_pa` | Tính `PA = frame * P + offset`. | `frame`, `page_size`, `offset`, `physical_address` |
| 7. `result` | Trả thành công hoặc mã lỗi. Luôn ghi bước này, kể cả khi dừng sớm. | `status`, `error` |

Với bảng mẫu có 4 entry, không gian địa chỉ được bảng bao phủ là 0–63. Trang 1 có bit valid bằng 0 nên vùng 16–31 bị từ chối. Ví dụ `37 → page 2, offset 5 → frame 7 → PA 117`. Tra mảng theo chỉ số có chi phí O(1) mỗi địa chỉ sau khi nạp bảng, theo giả định các phép toán số nguyên có chi phí hằng số.
