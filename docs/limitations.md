# Giới hạn của mô hình bảng trang một cấp (bản nháp của Đăng)

Chú thích trích dẫn: `[số, tr. x]` theo [references.md](references.md): [1] OSTEP, [2] Silberschatz *Operating System Concepts* 10th, [3] slide ch9 của thầy, [4] xv6 (MIT). Số thứ tự cuối cùng do Lý đánh lại. Câu không có trích dẫn là phân tích của nhóm. Phần B chỉ mô tả phạm vi của mô phỏng, căn cứ vào [specification.md](specification.md) (đọc, không chỉnh sửa).

Đề yêu cầu nêu giới hạn của mô hình page table một cấp. Báo cáo nên tách hai nhóm: giới hạn của **kỹ thuật** (có nguồn) và giới hạn của **mô phỏng của nhóm** (do phạm vi đề đặt ra).

## A. Giới hạn của bảng trang một cấp (theo nguồn)

### A1. Bảng trang rất lớn

Bảng một cấp là một mảng với một mục cho mỗi trang của không gian địa chỉ. Với không gian địa chỉ 32-bit, trang 4 KB, mỗi mục 4 byte: 2^20 (khoảng 1 triệu) mục, tức 4 MB cho mỗi tiến trình [2, tr. 371], [3, slide 39], [1, ch. 18, tr. 5], [1, ch. 20, tr. 1]. Với 100 tiến trình thì cần 400 MB chỉ cho các bảng trang [1, ch. 18, tr. 5]. Với không gian địa chỉ 64-bit, trang 4 KB, bảng có 2^52 mục [3, slide 43].

Giáo trình còn lưu ý không nên cấp phát bảng trang liên tục trong bộ nhớ chính vì kích thước này [2, tr. 371], [3, slide 39].

### A2. Lãng phí với không gian địa chỉ thưa

Bảng một cấp phải có đủ chỗ cho mọi trang, kể cả những trang không dùng. Ví dụ trong OSTEP: phần lớn bảng trang của một không gian địa chỉ nhỏ chỉ chứa các mục invalid, và "tốn chỗ" như vậy cũng xảy ra với không gian 32-bit [1, ch. 20, tr. 4]. Bit valid cho phép bỏ qua việc cấp frame cho các trang này [1, ch. 18, tr. 6], nhưng bản thân mục trong bảng vẫn tồn tại.

### A3. Thêm một lần truy cập bộ nhớ cho mỗi lần dịch

Bảng trang nằm trong bộ nhớ chính, nên mỗi lần truy cập dữ liệu cần hai lần truy cập bộ nhớ: một lần đọc mục trang, một lần đọc dữ liệu, làm chậm đi hệ số 2 [2, tr. 366], [3, slide 30], [1, ch. 18, tr. 8–9]. Phần cứng thường dùng TLB để giảm chi phí này; ví dụ trong slide: với tỷ lệ trúng TLB 80% và 10 ns mỗi lần truy cập bộ nhớ, thời gian truy cập hiệu dụng là 0,8 × 10 + 0,2 × 20 = 12 ns [3, slide 34]. TLB nằm ngoài phạm vi đồ án.

### A4. Phân mảnh trong và đánh đổi về kích thước trang

Frame được cấp theo đơn vị nguyên, nên frame cuối của tiến trình có thể không đầy. Trung bình mất nửa trang mỗi tiến trình [2, tr. 362–363], [3, slide 28]. Chọn trang lớn thì bảng nhỏ đi nhưng phân mảnh trong tăng: với không gian 32-bit, trang 16 KB (thay vì 4 KB) thì bảng giảm từ 4 MB xuống 1 MB [1, ch. 20, tr. 1–2]. Chọn trang nhỏ thì ngược lại, vì mỗi mục trong bảng tốn bộ nhớ [3, slide 28]. Vì vậy các hệ thống thường dùng trang tương đối nhỏ, như 4 KB hoặc 8 KB [1, ch. 20, tr. 2].

### A5. Hướng khắc phục (chỉ nêu, không triển khai)

Các cấu trúc bảng trang khác được dùng để giảm chi phí ở A1 và A2: bảng trang phân cấp, bảng băm, bảng nghịch đảo [2, tr. 371–375], [3, slide 39–47]. Hệ điều hành xv6 dùng cây ba cấp để bỏ qua các phần không dùng của không gian địa chỉ [4, tr. 32]. OSTEP còn mô tả cách kết hợp paging với segmentation [1, ch. 20, tr. 2]. Các kỹ thuật này nằm ngoài phạm vi đề bài.

## B. Giới hạn của mô phỏng của nhóm (phân tích của nhóm)

Căn cứ vào [specification.md](specification.md):

1. **Quy mô nhỏ:** mỗi lần chạy mô phỏng một không gian địa chỉ, một bảng trang một cấp và một kích thước trang cố định. Bảng mẫu có 4 mục với P = 16 byte. Chỉ để minh họa, không phản ánh quy mô thực tế (liên hệ A1).
2. **Không mô phỏng thời gian:** mô phỏng chỉ trả địa chỉ vật lý và trace, không đo số lần truy cập bộ nhớ hay độ trễ. Chi phí hai lần truy cập (A3) chỉ được nêu bằng lập luận, không đo bằng mô phỏng.
3. **Không giới hạn kích thước bộ nhớ vật lý:** đặc tả không đặt giới hạn trên cho số frame và cho địa chỉ logic, nên mô hình không kiểm tra frame có tồn tại trong bộ nhớ vật lý hay không.
4. **Chỉ có bit valid:** bit bảo vệ đọc/ghi/thực thi không được mô phỏng, mặc dù nguồn có nêu [2, tr. 368], [3, slide 35].
5. **Địa chỉ không hợp lệ chỉ trả mã lỗi:** mô phỏng không xử lý việc hệ điều hành bắt trap rồi làm gì tiếp, và không mô phỏng việc nạp trang vào frame. Các nội dung này nằm ngoài phạm vi đề (không yêu cầu page replacement, frame allocation).
6. **Nhiều trang có thể trỏ vào cùng một frame:** đặc tả cho phép, nhưng mô phỏng không mô hình hóa ý nghĩa chia sẻ (như chia sẻ mã giữa tiến trình [2, tr. 369–370]).
7. **Không có TLB, bảng nhiều cấp, cấp phát frame, thay trang:** loại trừ theo đề.

## Gợi ý cách viết trong báo cáo

- Mở đầu bằng A1 và A3, vì đây là hai giới hạn nổi bật nhất và có số liệu cụ thể (4 MB, hệ số 2).
- A2 và A4 viết ngắn, mỗi ý một đoạn.
- A5 một đoạn, nhấn mạnh đây là hướng mở rộng, không thuộc đồ án.
- Phần B viết như một danh sách "phạm vi và hạn chế của mô phỏng", nối với phần Kết luận.

## Ghi chú kiểm tra

- Mọi trang trích dẫn đã mở nguồn đọc lại. Số liệu đã đối chiếu: 2^20 mục và 4 MB ([2], [3], [1] đều khớp), 400 MB cho 100 tiến trình [1, ch. 18, tr. 5], 2^52 mục [3, slide 43], ví dụ 12 ns [3, slide 34], bảng 4 MB giảm còn 1 MB khi trang 16 KB [1, ch. 20, tr. 1].
- Các nguồn tính bảng 4 MB theo công thức 2^32 / 2^12 × 4 byte; kết quả khớp nhau.
- Khai báo AI trong báo cáo: Claude Code hỗ trợ đối chiếu nguồn và soạn nháp. Đăng chịu trách nhiệm đọc lại và hiểu toàn bộ nội dung.
