# Kiểm chứng độc lập – Paging và Page-Table Address Translation

Phần của Sơn: Kiểm thử và kiểm chứng. Tài liệu này đối chiếu ma trận test của nhóm (RESEARCH_PLAN.md, mục 7) bằng cách tính expected độc lập.

## 1. Giả định (suy ra từ ma trận của nhóm)

| Mục | Giá trị |
| --- | --- |
| Kích thước trang `P` | 16 byte |
| Đánh số page và frame | Bắt đầu từ 0 |
| Công thức | `page = floor(LA / P)`, `offset = LA mod P`, `PA = frame × P + offset` |
| Mã lỗi | `PAGE_OUT_OF_RANGE`, `INVALID_ENTRY`, `INVALID_ADDRESS` |

Page table suy ra từ expected của nhóm (cần đối chiếu với `docs/specification.md`):

| Page | Dải byte | Frame | Valid bit |
| --- | --- | --- | --- |
| 0 | 0 đến 15 | 3 | 1 |
| 1 | 16 đến 31 | không dùng | 0 |
| 2 | 32 đến 47 | 7 | 1 |
| 3 | 48 đến 63 | 0 | 1 |

Page table có 4 page, nên địa chỉ logic hợp lệ về phạm vi là 0 đến 63.

## 2. Ma trận test và kết quả tính độc lập

| ID | LA | Trường hợp | Expected của nhóm | Expected tính độc lập | Kết quả đối chiếu |
| --- | --- | --- | --- | --- | --- |
| T01 | 37 | Hợp lệ, page 2 | `PA = 117` | `PA = 117` | Khớp |
| T02 | 51 | Hợp lệ, page 3 | `PA = 3` | `PA = 3` | Khớp |
| T03 | 5 | Hợp lệ, page 0 | `PA = 53` | `PA = 53` | Khớp |
| T04 | 48 | Offset = 0 | `PA = 0` | `PA = 0` | Khớp |
| T05 | 63 | Offset = P − 1 | `PA = 15` | `PA = 15` | Khớp |
| T06 | 64 | Page ngoài bảng | `PAGE_OUT_OF_RANGE` | `PAGE_OUT_OF_RANGE` | Khớp |
| T07 | 16 | Entry invalid | `INVALID_ENTRY` | `INVALID_ENTRY` | Khớp |
| T08 | −1 | Địa chỉ âm | `INVALID_ADDRESS` | `INVALID_ADDRESS` | Khớp |

Đối chiếu yêu cầu của đề: 3 địa chỉ hợp lệ ở các page khác nhau (T01 page 2, T02 page 3, T03 page 0); offset = 0 (T04); offset = P − 1 (T05); page ngoài bảng (T06); entry không hợp lệ (T07); trường hợp biên nhóm chọn (T08).

Cột "Expected tính độc lập" tính bằng `expected_independent.py` theo cách khác với công thức của chương trình chính: duyệt từng page, xác định dải byte của page đó, rồi tính `offset = LA − đầu dải`. Cả 8 test khớp với expected nhóm đã ghi.

## 3. Bằng chứng tính tay (cách thứ hai, độc lập với script)

**T01 (hợp lệ):** `LA = 37`. Các dải byte: page 2 là 32 đến 47 nên `37` thuộc page 2, `offset = 37 − 32 = 5`. Page 2 có valid bit 1, frame 7, `PA = 7 × 16 + 5 = 117`.

**T07 (entry invalid):** `LA = 16`. Page 1 là 16 đến 31 nên `16` thuộc page 1, `offset = 16 − 16 = 0`. Page 1 có valid bit 0, trả `INVALID_ENTRY`, không tính địa chỉ vật lý.

**T06 (page ngoài bảng):** `LA = 64`. Dải cuối của bảng là 48 đến 63, `64` không thuộc dải nào, trả `PAGE_OUT_OF_RANGE`.

**T04 (có frame bằng 0):** `LA = 48`. Thuộc page 3 (48 đến 63), `offset = 0`, frame 0, `PA = 0 × 16 + 0 = 0`. Đây là trường hợp dễ sai: `PA = 0` là kết quả hợp lệ, không phải lỗi, nên chương trình không được coi giá trị 0 là "không có kết quả".

Các bằng chứng này gồm 3 trace chi tiết (T01 hợp lệ, T07 và T06 không hợp lệ), đủ yêu cầu "ít nhất 3 trace, có hợp lệ và không hợp lệ".

## 4. Kết quả chạy chương trình thật

Chương trình dịch địa chỉ được chạy bằng `python src/translate.py data/integration_cases.json` và đối chiếu với expected tính độc lập bằng `verify_actual.py`. Cả 8 test cho kết quả `actual` bằng `expected_independent`, ngoài ra các bước trong `trace` đúng thứ tự theo `docs/specification.md`. Bảng kết quả đầy đủ nằm trong `ket_qua_doi_chieu.csv`.

| ID | LA | Expected độc lập | Actual (chạy thật) | Pass/Fail |
| --- | --- | --- | --- | --- |
| T01 | 37 | 117 | 117 | PASS |
| T02 | 51 | 3 | 3 | PASS |
| T03 | 5 | 53 | 53 | PASS |
| T04 | 48 | 0 | 0 | PASS |
| T05 | 63 | 15 | 15 | PASS |
| T06 | 64 | `PAGE_OUT_OF_RANGE` | `PAGE_OUT_OF_RANGE` | PASS |
| T07 | 16 | `INVALID_ENTRY` | `INVALID_ENTRY` | PASS |
| T08 | −1 | `INVALID_ADDRESS` | `INVALID_ADDRESS` | PASS |

Bộ kiểm thử tích hợp của nhóm (`python tests/integration.py`) cũng báo 8/8 PASS.

Ba trace chi tiết lấy từ lần chạy thật nằm trong `data/traces/`: `trace_T01.json` (hợp lệ), `trace_T07.json` (entry invalid), `trace_T06.json` (page ngoài bảng).

## 5. Cách chạy lại kết quả kiểm chứng

Từ thư mục gốc của repo:

```
python verification/expected_independent.py
python src/translate.py data/integration_cases.json > ket_qua_chay_that.json
python verification/verify_actual.py ket_qua_chay_that.json
```

Lệnh đầu tính expected độc lập và ghi `verification/expected_results.csv`. Lệnh thứ hai chạy chương trình thật. Lệnh thứ ba đối chiếu và ghi `verification/ket_qua_doi_chieu.csv`. (Trên Windows dùng `python`; nếu lưu file bị lỗi font thì dùng `| Out-File -Encoding utf8` thay cho `>`.)

## 6. Giới hạn của bộ kiểm chứng

Bộ kiểm chứng chỉ bao phủ 8 test của ma trận. Các trường hợp đặc tả có nêu nhưng chưa được kiểm thử: địa chỉ kiểu số thực, chuỗi hoặc boolean; bảng trang rỗng; cấu hình JSON sai.
