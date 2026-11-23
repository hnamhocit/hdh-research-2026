# Review chéo của Đăng: giải thuật, thuật ngữ và kết quả

Ngày 23/11/2026. Đối tượng review (chỉ đọc, không chỉnh sửa): [pseudocode.md](pseudocode.md), [specification.md](specification.md), [`src/translate.py`](../src/translate.py), [`data/integration_cases.json`](../data/integration_cases.json), [`data/expected_results.json`](../data/expected_results.json). Đối chiếu với bản lý thuyết [theory.md](theory.md) và các nguồn trong [references.md](references.md).

Kết quả chạy lại: `python3 tests/integration.py` cho 8/8 ca PASS (T01–T08). Lệnh không làm thay đổi file nào đang được theo dõi trong git.

## 1. Đối chiếu giải thuật với đề và với nguồn

| Bước trong đề | Bước trong đặc tả/simulator | Căn cứ lý thuyết | Nhận xét |
|---|---|---|---|
| — | 1. `validate_address` | Không có trong nguồn | Bước nhóm thêm để xử lý LA âm (ca T08) hoặc sai kiểu (chưa có ca kiểm thử cho sai kiểu). Hợp lý, nên ghi trong báo cáo là quy ước của nhóm. |
| 1. Tách page number và offset | 2. `split`: `divmod(LA, P)` | [2, tr. 360–361], [1, ch. 18, tr. 3–4] | Khớp. Với P lũy thừa của 2, phép chia và lấy dư tương đương với tách bit cao/thấp (nhóm suy ra; cơ sở tách bit: [2, tr. 361]). |
| 2. Kiểm tra page có trong bảng | 3. `check_page`: `page < len(table)` | Tương ứng PTLR [2, tr. 369], [3, slide 35] | Khớp. Nên ghi trong báo cáo rằng bước này mô phỏng vai trò của PTLR. |
| 3. Kiểm tra valid/invalid bit | 4. `check_valid` | [2, tr. 368–369], [1, ch. 18, tr. 6, 9] | Khớp. Thứ tự "kiểm tra phạm vi trước, valid sau" là cần thiết vì không thể đọc `table[page]` khi page ngoài bảng. |
| 4. Lấy frame number | 5. `read_frame` | [2, tr. 361] | Khớp. |
| 5. Tính physical address | 6. `compute_pa`: `frame * P + offset` | [2, tr. 361], [1, ch. 18, tr. 5] | Khớp, offset giữ nguyên. |
| 6. Trả kết quả hoặc invalid/page fault | 7. `result` | — | Khớp. Xem mục 2 về cách gọi lỗi. |

Kiểm tra số liệu: LA 37 → page 2, offset 5, frame 7, PA 117 trùng với ví dụ trong đề. Các kết quả dự kiến khác cũng khớp với công thức `PA = frame × 16 + offset` theo bảng mẫu (page 0 → frame 3, page 1 invalid, page 2 → frame 7, page 3 → frame 0).

## 2. Thuật ngữ cần thống nhất trong báo cáo

| Khái niệm | Code/đặc tả | Bản lý thuyết | Nguồn | Đề xuất dùng trong báo cáo |
|---|---|---|---|---|
| Logical address | `logical_address`, LA | địa chỉ logic (LA) | logical address [2], virtual address [1], [4] | "địa chỉ logic (LA)"; ghi chú một lần rằng [1], [4] gọi là địa chỉ ảo |
| Page number | `page` | số trang p | page number p [2]; VPN [1] | "số trang (page number) p" |
| Offset | `offset` | độ dời d | page offset d [2]; offset [1] | "độ dời (offset) d" |
| Frame number | `frame` | số frame f | frame number f [2]; PFN [1] | "số frame f" |
| Bit hợp lệ | `valid` (0/1) | bit valid/invalid | valid–invalid bit [2]; valid bit [1]; `PTE_V` [4] | "bit valid–invalid" |
| Lỗi page ngoài bảng | `PAGE_OUT_OF_RANGE` | — | trap khi vượt PTLR [2, tr. 369] | giữ mã lỗi của nhóm, giải thích bằng PTLR |
| Lỗi entry invalid | `INVALID_ENTRY` | — | trap "invalid page reference" [2, tr. 369]; `SEGMENTATION_FAULT` [1, ch. 18, tr. 9]; "page-fault exception" [4, tr. 32] | giữ mã lỗi, giải thích là "truy cập trang không hợp lệ" |

**Lưu ý về chữ "page fault":** đề viết "invalid/page fault". Các nguồn gọi trường hợp bit invalid theo những cách khác nhau: [2, tr. 369] gọi là trap "invalid page reference", [1, ch. 18, tr. 9] phát sinh `SEGMENTATION_FAULT`, còn [4, tr. 32] gọi là "page-fault exception" và để kernel xử lý. Mô phỏng không xử lý ngoại lệ và không nạp trang từ đĩa, nên báo cáo không nên khẳng định `INVALID_ENTRY` là page fault theo nghĩa demand paging. Đề xuất viết: "trường hợp mà đề gọi là invalid/page fault, trong mô hình được báo bằng `INVALID_ENTRY`".

## 3. Nhận xét về độ phức tạp trong pseudocode

Pseudocode ghi mỗi lần dịch là O(1) theo mô hình chi phí hằng số. Nhận định này nhất quán với nguồn: bảng một cấp được tra trực tiếp theo chỉ số, nên chỉ cần một lần đọc mục trang [1, ch. 18, tr. 8–9]. Đề xuất bổ sung một câu nối với lý thuyết: O(1) ở đây vẫn tương ứng với một lần truy cập bộ nhớ thêm cho mỗi lần dịch, làm chậm hệ số 2 so với không phân trang [2, tr. 366]. Với bảng nhiều cấp như xv6, CPU phải đọc ba mục cho mỗi lần dịch [4, tr. 32].

## 4. Các điểm cần nhóm xác nhận (không phải lỗi)

1. Đặc tả cho phép nhiều trang trỏ vào cùng frame và không giới hạn số frame. Phần giới hạn ([limitations.md](limitations.md), mục B) đã ghi nhận, Cần Nam và Minh xác nhận đây là chủ ý (repo chưa ghi xác nhận này; đầu specification.md vẫn ghi Minh và Sơn cần xác nhận hợp đồng).
2. `valid_entry` trong simulator chỉ nhận `valid` là số nguyên 0 hoặc 1, nên `true`/`false` trong JSON bị từ chối với mã `INVALID_INPUT`. Khớp với đặc tả ("giá trị boolean không được coi là số nguyên"). Nên nêu một câu trong phần giả định của báo cáo.
3. Ví dụ OSTEP [1, ch. 18, tr. 3–5] cũng ra PA 117 nhưng với LA 21 (page 1 → frame 7). Khi Lý đưa vào báo cáo cần ghi rõ ví dụ nào của đề, ví dụ nào của nguồn.

Không phát hiện sai lệch nào giữa đặc tả, pseudocode, simulator và lý thuyết.
