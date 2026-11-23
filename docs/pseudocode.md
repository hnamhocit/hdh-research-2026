# Giải thuật dịch địa chỉ

Kiểm tra cấu hình khi nạp file. Với từng LA, chạy các bước sau, ghi trace theo [đặc tả](specification.md). Mỗi lệnh trả kết quả ghi thêm bước `result`.

```text
TRANSLATE(LA, P, table)
    nếu LA không phải số nguyên không âm
        trả INVALID_ADDRESS

    page ← thương nguyên của LA chia P
    offset ← số dư của LA chia P
    nếu page ≥ số entry trong table
        trả PAGE_OUT_OF_RANGE cùng page, offset

    entry ← table[page]
    nếu entry.valid = 0
        trả INVALID_ENTRY cùng page, offset

    frame ← entry.frame
    PA ← frame × P + offset
    trả OK cùng page, offset, frame, PA
```

Sau khi nạp bảng, mỗi lần dịch dùng một lần tra mảng và số bước cố định. Theo mô hình chi phí hằng số cho các phép toán số nguyên, thời gian và bộ nhớ bổ sung mỗi lần dịch đều là O(1), kể cả trace có tối đa bảy bước. Bảng chiếm O(N) với N entry. CLI giữ O(M) kết quả trước khi ghi JSON cho M địa chỉ.
