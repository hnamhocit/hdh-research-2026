# Đối chiếu độc lập theo dải byte

Với trang 16 byte, viết các dải liên tiếp (mỗi dải chứa 16 byte) và đọc vị trí tương ứng trong hai dải. Bảng dưới cho expected của bộ tích hợp. Có thể đối chiếu với [actual](../data/actual_results.json) mà không cần đọc mã mô phỏng.

| ID | LA | Cách đọc từ dải byte | Expected |
|---|---:|---|---|
| T01 | 37 | Dải logic 32–47 ghép với dải vật lý 112–127. Byte thứ 6 ứng với 117. | Trang 2, offset 5, frame 7, PA 117 |
| T02 | 51 | Dải logic 48–63 ghép với dải vật lý 0–15. Byte thứ 4 ứng với 3. | Trang 3, offset 3, frame 0, PA 3 |
| T03 | 5 | Dải logic 0–15 ghép với dải vật lý 48–63. Byte thứ 6 ứng với 53. | Trang 0, offset 5, frame 3, PA 53 |
| T04 | 48 | Byte đầu của dải logic 48–63 ứng với byte đầu của dải vật lý 0–15. | Trang 3, offset 0, frame 0, PA 0 |
| T05 | 63 | Byte cuối của dải logic 48–63 ứng với byte cuối của dải vật lý 0–15. | Trang 3, offset 15, frame 0, PA 15 |
| T06 | 64 | Là byte đầu của dải 64–79, nằm ngay sau bốn dải có trong bảng. | Trang 4, offset 0, `PAGE_OUT_OF_RANGE` |
| T07 | 16 | Là byte đầu của dải 16–31. Dải có entry với bit valid 0. | Trang 1, offset 0, `INVALID_ENTRY` |
| T08 | −1 | Nằm trước byte đầu tiên của không gian địa chỉ logic. | `INVALID_ADDRESS` |
