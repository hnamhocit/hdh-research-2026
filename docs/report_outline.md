# Báo cáo nghiên cứu — Paging and Page-Table Address Translation

## Quy chuẩn chung
- **Độ dài nội dung chính:** 6–10 trang.
- **Trích dẫn:** Chuẩn IEEE (đánh số trong ngoặc vuông `[1]`, `[2]`...).
- **Thuật ngữ & Mã lỗi:** Giữ nguyên tiếng Anh (`LA`, `PA`, `Page`, `Frame`, `Offset`, `INVALID_ADDRESS`, `PAGE_OUT_OF_RANGE`, `INVALID_ENTRY`).

---

## Bảng thuật ngữ dùng trong bài

| Thuật ngữ / Ký hiệu | Nghĩa tiếng Việt | Giải thích ngắn gọn |
| :--- | :--- | :--- |
| **LA** (Logical Address) | Địa chỉ logic | Địa chỉ do CPU tạo ra trong quá trình chạy chương trình (đơn vị: byte). |
| **PA** (Physical Address) | Địa chỉ vật lý | Địa chỉ thực tế trên thanh RAM (đơn vị: byte). |
| **P** (Page Size) | Kích thước trang | Kích thước cố định của một page hoặc frame, chọn là lũy thừa của 2 ($P = 16\text{ bytes}$). |
| **Page Number ($p$)** | Số thứ tự trang | Vị trí của trang trong bộ nhớ logic ($p = \lfloor \text{LA} / P \rfloor$). |
| **Offset ($d$)** | Độ dời | Vị trí của byte nằm bên trong trang ($d = \text{LA} \bmod P$, với $0 \le d \le P - 1$). |
| **Frame Number ($f$)** | Số thứ tự khung trang | Vị trí của khung trang tương ứng trên bộ nhớ vật lý (RAM). |
| **Valid/Invalid Bit** | Bit hợp lệ | Cờ báo hiệu trang có được phép truy cập hay không (`1`: hợp lệ, `0`: không hợp lệ). |

---

## 1. Câu hỏi nghiên cứu và phạm vi

### 1.1. Đặt vấn đề
Trong các hệ điều hành hiện đại, chương trình khi chạy không làm việc trực tiếp với địa chỉ thật trên RAM mà dùng địa chỉ logic (LA) do CPU tạo ra. Để tránh phân mảnh ngoại vi và không bắt buộc cấp phát bộ nhớ liên tục, cơ chế phân trang (Paging) chia không gian địa chỉ logic thành các trang (page) và bộ nhớ vật lý thành các khung trang (frame) có kích thước bằng nhau. Đồ án này tìm hiểu và mô phỏng quá trình đổi địa chỉ logic sang địa chỉ vật lý qua bảng trang một cấp (single-level page table), kèm bộ kiểm thử và đối chiếu tính tay độc lập.

### 1.2. Hai câu hỏi nghiên cứu trọng tâm
1. Với bảng trang một cấp, địa chỉ logic (LA) được đổi sang địa chỉ vật lý (PA) theo quy trình gồm những bước nào?
2. Trong những trường hợp nào một địa chỉ logic bị xác định là không hợp lệ?

### 1.3. Phạm vi đề tài
- **Phần thực hiện:** Bảng trang một cấp, kích thước trang $P$ cố định (lũy thừa của 2), kiểm tra bit `valid/invalid`, giải thuật dịch 6 bước, xuất trace từng bước, chạy tối thiểu 8 test cases và kiểm chứng độc lập bằng tính tay.
- **Phần không thực hiện:** Không triển khai TLB, bảng trang nhiều cấp, thuật toán thay thế trang, thrashing hay giao diện đồ họa (GUI).

---

## 2. Cơ sở lý thuyết


---

## 3. Mô hình và giả định

### 3.1. Các giả định hệ thống
- **Đơn vị đo:** Tất cả địa chỉ (LA, PA) và kích thước trang ($P$) đều tính bằng **byte**.
- **Kích thước trang ($P$):** Chọn $P = 16\text{ bytes}$ ($2^4$) và giữ cố định trong suốt bộ test.
- **Quy ước đánh số:** Số thứ tự trang (`page_number`) và khung trang (`frame_number`) đều đếm từ `0` (`0, 1, 2,...`).
- **Cấu trúc bảng trang:** Bảng trang một cấp gồm 4 dòng cố định (từ `page 0` đến `page 3`), mỗi dòng lưu bit `valid` (`1` hoặc `0`) và `frame_number`.

### 3.2. Công thức dịch địa chỉ
- $\text{page\_number} = \lfloor \text{LA} / P \rfloor$
- $\text{offset} = \text{LA} \bmod P$
- $\text{PA} = \text{frame\_number} \times P + \text{offset}$ (nếu entry hợp lệ)

### 3.3. Bảng trang mẫu và quy ước mã lỗi

| Page Number | Valid Bit | Frame Number | Trạng thái |
| :---: | :---: | :---: | :--- |
| 0 | 1 | 3 | Hợp lệ, trỏ tới frame 3 |
| 1 | 0 | — | Không hợp lệ (`valid = 0`) |
| 2 | 1 | 7 | Hợp lệ, trỏ tới frame 7 |
| 3 | 1 | 0 | Hợp lệ, trỏ tới frame 0 |

- `INVALID_ADDRESS`: Địa chỉ đầu vào bị âm ($\text{LA} < 0$).
- `PAGE_OUT_OF_RANGE`: Số trang tính được vượt ngoài bảng trang ($\text{page\_number} \ge 4$).
- `INVALID_ENTRY`: Số trang nằm trong bảng nhưng có `valid = 0`.

---

## 4. Giải thuật


---

## 5. Kết quả và trace


### 5.1. Bảng kết quả 8 trường hợp kiểm thử

| ID | Trường hợp kiểm thử | Input (LA) | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :---: | :--- | :--- | :---: |
| T01 | Địa chỉ hợp lệ thuộc page 2 | 37 | PA 117 | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T02 | Địa chỉ hợp lệ thuộc page 3 | 51 | PA 3 | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T03 | Địa chỉ hợp lệ thuộc page 0 | 5 | PA 53 | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T04 | Trường hợp biên `offset = 0` | 48 | PA 0 | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T05 | Trường hợp biên `offset = P - 1` | 63 | PA 15 | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T06 | Số trang nằm ngoài bảng trang | 64 | `PAGE_OUT_OF_RANGE` | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T07 | Mục bảng trang không hợp lệ (`valid = 0`) | 16 | `INVALID_ENTRY` | *(Chờ chạy cuối)* | *(PASS/FAIL)* |
| T08 | Trường hợp biên tự chọn (địa chỉ âm) | -1 | `INVALID_ADDRESS` | *(Chờ chạy cuối)* | *(PASS/FAIL)* |

### 5.2. Trace chi tiết từng bước (Tối thiểu 3 trường hợp)


---

## 6. Kiểm chứng độc lập

### 6.1. Phương pháp kiểm chứng
Để đảm bảo chương trình mô phỏng tính toán đúng theo lý thuyết và không mắc lỗi lập trình, kết quả đầu ra được đối chiếu bằng cách tính tay độc lập (tách biệt hoàn toàn khỏi mã nguồn `src/translate.py`). Các bước tính tay áp dụng trực tiếp công thức toán học với kích thước trang $P = 16\text{ bytes}$ trên 3 trường hợp tiêu biểu: một địa chỉ hợp lệ (`T01`), một địa chỉ biên (`T05`) và một địa chỉ truy cập vào mục bảng trang không hợp lệ (`T07`).

### 6.2. Bảng đối chiếu kết quả tính tay và chương trình mô phỏng

| Test ID | Input (LA) | Phép tính độc lập (Tính tay theo công thức) | Expected độc lập | Actual từ Simulator | Khớp kết quả |
| :--- | :---: | :--- | :--- | :--- | :---: |
| **T01** | 37 | $\lfloor 37/16 \rfloor = 2$; $37 \bmod 16 = 5$. Tra bảng: Page 2 $\rightarrow$ Frame 7 (`valid = 1`). Tính $\text{PA} = 7 \times 16 + 5 = 117$. | PA 117 | PA 117 | Khớp |
| **T05** | 63 | $\lfloor 63/16 \rfloor = 3$; $63 \bmod 16 = 15$. Tra bảng: Page 3 $\rightarrow$ Frame 0 (`valid = 1`). Tính $\text{PA} = 0 \times 16 + 15 = 15$. | PA 15 | PA 15 | Khớp |
| **T07** | 16 | $\lfloor 16/16 \rfloor = 1$; $16 \bmod 16 = 0$. Tra bảng: Page 1 có `valid = 0` $\rightarrow$ Dừng và trả mã lỗi. | `INVALID_ENTRY` | `INVALID_ENTRY` | Khớp |

---

## 7. Phân tích
- **7.1. Độ phức tạp thuật toán:** Thời gian $O(1)$, không gian $O(N)$ 
- **7.2. So sánh Paging một cấp với Segmentation / Base-Limit relocation** 

---

## 8. Giới hạn của mô hình

---

## 9. Kết luận


---

## 10. Tài liệu tham khảo


---

## Phụ lục
- Bảng phân công và mức độ đóng góp thực tế của 5 thành viên.
- Khai báo công cụ AI và mục đích sử dụng.