# So sánh phân trang (paging) với base/limit relocation (bản nháp của Đăng)

Chú thích trích dẫn: `[số, tr. x]` theo [references.md](references.md): [1] OSTEP, [2] Silberschatz *Operating System Concepts* 10th, [3] slide ch9 của thầy. Số thứ tự cuối cùng do Lý đánh lại. Câu không có trích dẫn là phân tích của nhóm, không phải của nguồn. Số bảng sẽ đánh theo chương khi đưa vào báo cáo.

## Hai cơ chế được so sánh

- **Base/limit relocation:** phần cứng có một cặp thanh ghi cho mỗi CPU [1, ch. 15, tr. 7], được nạp giá trị của tiến trình đang chạy. Thanh ghi relocation (base) chứa địa chỉ vật lý nhỏ nhất, thanh ghi limit chứa dải địa chỉ logic. MMU cộng giá trị base vào địa chỉ logic, và mỗi địa chỉ logic phải nằm trong giới hạn [2, tr. 357], [3, slide 17], [1, ch. 15, tr. 7].
- **Phân trang một cấp:** tách địa chỉ logic thành số trang và độ dời, tra bảng trang để thay số trang bằng số frame, giữ nguyên độ dời [2, tr. 361] (xem [theory.md](theory.md), mục 2.3–2.4).

## Bảng so sánh theo 5 tiêu chí

| Tiêu chí | Base/limit relocation | Phân trang một cấp |
|---|---|---|
| **1. Cách dịch địa chỉ và phần cứng cần** | `PA = LA + base`, kiểm tra `LA < limit` [1, ch. 15, tr. 6–7]. Cần một cặp thanh ghi trong CPU, mạch cộng và mạch so sánh, được mô tả là "khá đơn giản" [1, ch. 15, tr. 8–9]. Khi chuyển ngữ cảnh chỉ cần nạp lại cặp thanh ghi [2, tr. 357], [1, ch. 15, tr. 10]. | Tách p và d, tra bảng trang theo chỉ số p, thay p bằng f, `PA = f × P + offset` [2, tr. 361–362]. Cần bảng trang trong bộ nhớ và thanh ghi PTBR trỏ tới bảng, có thể thêm PTLR [2, tr. 365, 369], [3, slide 30]. |
| **2. Cách đặt tiến trình trong bộ nhớ vật lý** | Mỗi tiến trình nằm trong một vùng liên tục [2, tr. 357], [3, slide 16]. | Các page đặt vào frame bất kỳ còn trống, không cần liền nhau [2, tr. 360], [3, slide 23]. |
| **3. Phân mảnh** | Phân mảnh ngoài (external) khi các lỗ trống bị chia nhỏ và không liền nhau [2, tr. 359], [3, slide 21]. Có thể giảm bằng dồn bộ nhớ (compaction), nhưng chỉ làm được khi relocation là động [2, tr. 360], [3, slide 22]. Nếu mỗi tiến trình nằm trong khe cố định, khoảng trống giữa stack và heap bị lãng phí (phân mảnh trong) [1, ch. 15, tr. 13]. | Không có phân mảnh ngoài [2, tr. 360, 362], [3, slide 23], [1, ch. 18, tr. 12]. Còn phân mảnh trong: frame cuối của tiến trình có thể không đầy, trung bình mất nửa trang mỗi tiến trình [2, tr. 362–363], [3, slide 23, 28]. |
| **4. Bảo vệ và phát hiện địa chỉ không hợp lệ** | So địa chỉ với thanh ghi limit; địa chỉ vượt giới hạn hoặc âm thì CPU phát sinh exception [1, ch. 15, tr. 7], [2, tr. 357]. Chỉ có một phép kiểm tra cho cả vùng của tiến trình (suy ra từ mô tả này). | Bit valid–invalid cho từng trang, truy cập trang invalid thì trap vào hệ điều hành [2, tr. 368–369], [3, slide 35]. Có thể kiểm tra thêm độ dài bảng bằng PTLR [2, tr. 369]. Thêm bit bảo vệ cho từng frame (chỉ đọc, đọc–ghi) [2, tr. 368], [3, slide 35]. Kiểm tra được từng trang, tinh hơn so với một giới hạn duy nhất. |
| **5. Chi phí truy cập bộ nhớ và bộ nhớ cho cấu trúc quản lý** | Hai thanh ghi nằm trên chip [1, ch. 15, tr. 7], nên phép dịch không cần đọc bảng trong bộ nhớ (suy ra từ mô tả này). Mỗi tiến trình chỉ cần lưu hai giá trị base/limit, nạp lại vào thanh ghi khi chuyển ngữ cảnh [1, ch. 15, tr. 7, 10]. | Bảng trang nằm trong bộ nhớ chính, nên mỗi lần truy cập dữ liệu cần hai lần truy cập bộ nhớ, chậm đi hệ số 2 [2, tr. 366], [3, slide 30], [1, ch. 18, tr. 8–9]. Bảng trang tốn bộ nhớ: hệ thống 32-bit, trang 4 KB, mỗi mục 4 byte thì mỗi tiến trình cần tới 4 MB cho bảng [2, tr. 371], [3, slide 39]. |

## Tiêu chí bổ sung (chưa đưa vào bảng chính)

- **Chia sẻ mã giữa các tiến trình:** với phân trang, nhiều tiến trình có thể cùng ánh xạ các trang của một đoạn mã không tự sửa (reentrant), chỉ cần một bản trong bộ nhớ vật lý [2, tr. 369–370], [3, slide 37]. Ví dụ giáo trình: 40 tiến trình dùng thư viện libc 2 MB, nếu mỗi tiến trình nạp riêng thì cần 80 MB [2, tr. 370]. Các chương đã đọc của nguồn [1] không bàn đến chia sẻ ở mức base/limit, nên bảng này không kết luận về cơ chế base/limit ở tiêu chí này.
- **Segmentation (tham khảo thêm):** mỗi segment logic có cặp base/bounds riêng, khắc phục việc lãng phí khoảng trống giữa stack và heap [1, ch. 16, tr. 1–2]. Vì các segment có độ dài thay đổi, phân mảnh ngoài vẫn xảy ra [1, ch. 16, tr. 10]. Chia sẻ mã được hỗ trợ bằng bit bảo vệ cho từng segment [1, ch. 16, tr. 7]. Đề cho phép chọn segmentation hoặc base/limit, nhóm dùng base/limit làm đối tượng so sánh chính.

## Nhận xét ngắn (phân tích của nhóm, dựa trên các dòng trong bảng)

- Base/limit đơn giản và nhanh nhưng đòi hỏi vùng nhớ liên tục, nên dễ phân mảnh ngoài và lãng phí khi không gian địa chỉ thưa.
- Phân trang bỏ yêu cầu liên tục và tránh phân mảnh ngoài, kiểm tra hợp lệ được từng trang, đổi lại tốn thêm bộ nhớ cho bảng trang và thêm một lần truy cập bộ nhớ cho mỗi lần dịch nếu không có TLB.
- Trong hai trường hợp lỗi của mô hình nhóm, `PAGE_OUT_OF_RANGE` (số trang ≥ số mục) là cùng loại kiểm tra độ dài như thanh ghi limit của base/limit và như PTLR [2, tr. 369]. Chỉ `INVALID_ENTRY` (bit valid của từng trang) là không có tương ứng trong base/limit.

## Ghi chú kiểm tra

- Mọi trang trích dẫn đã mở nguồn đọc lại. Riêng ô "không cần đọc bảng trong bộ nhớ" ở tiêu chí 5 của base/limit là suy ra từ việc thanh ghi nằm trên chip, và đã ghi rõ trong bảng.
- Chương 15 và 20 của [1] bản tải về ghi bản quyền 2008–23, chương 16 và 18 ghi 2008–25 (đều là Version 1.10). Đây là cách OSTEP cập nhật từng chương, không ảnh hưởng nội dung được trích.
- Phần so sánh này chưa bàn về TLB vì TLB nằm ngoài phạm vi đồ án.
- Khai báo AI trong báo cáo: Claude Code hỗ trợ đối chiếu nguồn và soạn nháp bảng. Đăng chịu trách nhiệm đọc lại và hiểu toàn bộ nội dung.
