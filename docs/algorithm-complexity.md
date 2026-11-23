# Giải thuật mô phỏng & Phân tích độ phức tạp (Minh)

## 1. Pseudocode dịch địa chỉ Logical Address -> Physical Address

```text
FUNCTION TranslateAddress(logical_address, page_size, page_table):
    IF logical_address < 0 OR logical_address IS NOT INTEGER:
        RETURN ERROR("INVALID_ADDRESS")

    page_number = FLOOR(logical_address / page_size)
    offset = logical_address MOD page_size

    IF page_number >= LENGTH(page_table):
        RETURN ERROR("PAGE_OUT_OF_RANGE")

    entry = page_table[page_number]
    IF entry.valid == FALSE:
        RETURN ERROR("INVALID_ENTRY")

    physical_address = entry.frame * page_size + offset
    RETURN SUCCESS(physical_address)
END FUNCTION
```

## 2. Phân tích độ phức tạp

Với bảng trang một cấp gồm $N$ mục (entries) và kích thước trang $P = 2^k$:
* **Độ phức tạp thời gian (Time Complexity): $\mathcal{O}(1)$**
  * Tách `page_number` và `offset` bằng phép chia nguyên và chia lấy dư mất $\mathcal{O}(1)$.
  * Tra cứu trực tiếp mảng `page_table[page_number]` và kiểm tra bit `valid` mất $\mathcal{O}(1)$ (giả định bảng trang nằm sẵn trong bộ nhớ chính, không tính độ trễ đĩa hay TLB).
  * Tính `physical_address = frame * P + offset` mất $\mathcal{O}(1)$.
  * Khi chạy lô $M$ địa chỉ kiểm thử, tổng thời gian là $\mathcal{O}(M)$.
* **Độ phức tạp không gian (Space Complexity): $\mathcal{O}(N)$**
  * Bảng trang một cấp lưu trữ toàn bộ $N$ mục của không gian địa chỉ logic (gồm cả các trang chưa cấp phát có `valid = 0`), tốn $\mathcal{O}(N)$ bộ nhớ.
  * Bộ nhớ phụ trợ cho mỗi lần dịch địa chỉ chỉ dùng các biến cục bộ hằng số $\mathcal{O}(1)$.
