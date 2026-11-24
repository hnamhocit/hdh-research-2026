# Tài liệu tham khảo (Đăng)

Quy ước: ✅ đã mở file nguồn và đọc đúng đoạn được ghi. Mẫu trích dẫn theo hướng dẫn của trường (BM-BTL-07): `[số, tr. x-y]`, xếp ABC theo họ tác giả đầu.

## Danh mục (tiếng Anh)

[1] Arpaci-Dusseau R.H., Arpaci-Dusseau A.C. (2023). *Operating Systems: Three Easy Pieces*, Version 1.10, Arpaci-Dusseau Books. Dùng Chương 15 "Mechanism: Address Translation", Chương 16 "Segmentation", Chương 18 "Paging: Introduction", Chương 20 "Paging: Smaller Tables". http://ostep.org ✅
- Các chương đã đọc đều ghi `[VERSION 1.10]` (chương 15, 20 © 2008–23; chương 16, 18 © 2008–25). File lời nói đầu tải về là bản mới hơn ([VERSION 1.20], © 2008–26) nhưng danh sách trích dẫn trong đó chưa có v1.20; các chương được trích là v1.10 nên trích v1.10. Lời nói đầu ghi cách trích dẫn chính thức: 8/2018 (v1.00), 7/2019 (v1.01) hoặc 10/2023 (v1.10); bản đã đọc là v1.10 nên ghi năm 2023. Sách không ghi nơi xuất bản. Ngày truy cập: 23/11/2026.
- Số trang bên dưới là số in trong file chương. Mục lục sách: chương 15 bắt đầu tr. 153, chương 16 tr. 169, chương 18 tr. 199, chương 20 tr. 231.
- Sách phát miễn phí theo từng chương tại http://ostep.org (không đưa file vào repo).

[2] Silberschatz A., Galvin P.B., Gagne G. (2018). *Operating System Concepts*, 10th ed., Wiley, Hoboken NJ. Chương 9 "Main Memory". ✅ (nhà xuất bản và nơi xuất bản đã kiểm tra ở trang bản quyền của sách; số trang là số in trên sách = số trang file PDF trừ 106)

[3] Silberschatz A., Galvin P.B., Gagne G. (2018). *Chapter 9: Main Memory* (slide `ch9.pptx`, học phần Hệ điều hành 012012500102, giảng viên Mai Ngọc Châu), Trường ĐH GTVT TP.HCM, https://courses.ut.edu.vn. ✅ (chân slide trong slide master của file ghi "Silberschatz, Galvin and Gagne ©2018"; mã học phần và tên giảng viên lấy từ trang môn học trên eLearning; slide 25, 26, 33, 36 chỉ có tiêu đề và hình)

[4] Cox R., Kaashoek F., Morris R. (2024). *xv6: a simple, Unix-like teaching operating system*, (trang bìa ghi ngày 31/08/2024; "rev4" lấy từ tên file trên trang MIT), tài liệu trực tuyến của MIT (không ghi nhà xuất bản, nơi xuất bản). Dùng Chương 3 "Page tables". https://pdos.csail.mit.edu/6.1810/2024/xv6/book-riscv-rev4.pdf ✅ (tải miễn phí từ trang môn học 6.1810 của MIT, đã đọc chương 3. Số trang in = số trang file PDF. Ngày truy cập 23/11/2026.)
- Lưu ý: xv6 dùng bảng trang **ba cấp** (RISC-V Sv39), không phải một cấp. Chỉ trích cho các ý chung (trang 4096 byte, offset 12 bit, bit valid) và cho phần giới hạn/mở rộng của mô hình một cấp. Không trích như mô hình một cấp.

## Bảng tra cứu: ý nào lấy từ đâu (chỉ các chỗ đã đọc)

| Ý trong báo cáo | Nguồn | Vị trí đã đọc |
|---|---|---|
| Logical address và physical address, MMU | [2] | mục 9.1.3, tr. 353–354 |
| Thanh ghi base và limit | [2] | mục 9.1.1, tr. 351 |
| Relocation register + limit register bảo vệ bộ nhớ, MMU cộng relocation vào logical address | [2], [3], [1] | [2] mục 9.2.1 tr. 357. [3] slide 17. [1] ch.15 tr. 5–7 |
| External fragmentation ở cấp phát liên tục | [2], [3] | [2] mục 9.2.3 tr. 359. [3] slide 21 (định nghĩa) |
| External fragmentation ở segmentation (segment có kích thước thay đổi) | [1] | ch.16 tr. 9–10 |
| Paging: frame và page cùng kích thước | [2], [3], [1] | [2] tr. 360. [3] slide 23. [1] ch.18 tr. 1 |
| Kích thước trang là lũy thừa của 2 | [2], [3] | [2] tr. 361: "4 KB đến 1 GB". [3] slide 23: "512 byte đến 16 MB". Hai nguồn nêu khoảng khác nhau, trích nguồn nào ghi nguồn đó |
| Tách địa chỉ thành page number p và offset d; thay p bằng frame f, offset giữ nguyên | [2], [3], [1] | [2] tr. 360–361. [3] slide 24. [1] ch.18 tr. 3–5 |
| Ví dụ: không gian 64 byte, trang 16 byte, địa chỉ 21 → VPN 1, offset 5, frame 7, PA 117 | [1] | ch.18 tr. 3–5 (page table `3 7 5 2`) |
| Ví dụ: trang 4 byte, địa chỉ 0 → frame 5 → 20; địa chỉ 4 → frame 6 → 24 | [2] | tr. 362 |
| Page table riêng cho từng tiến trình | [2], [1] | [2] tr. 361. [1] ch.18 tr. 3 |
| `PTEAddr = PTBR + VPN × sizeof(PTE)`, `PhysAddr = (PFN << SHIFT) \| offset` | [1] | ch.18 tr. 8–9 (Hình 18.6) |
| Page table nằm trong bộ nhớ chính, có PTBR | [2], [3] | [2] tr. 365. [3] slide 30 |
| Mỗi truy cập dữ liệu cần hai lần truy cập bộ nhớ, chậm hệ số 2 | [2], [3], [1] | [2] tr. 366. [3] slide 30. [1] ch.18 tr. 8–9 |
| Valid–invalid bit: valid = trang thuộc không gian địa chỉ logic của tiến trình; invalid = không thuộc, truy cập sẽ trap | [2], [3], [1] | [2] mục 9.3.3 tr. 368–369. [3] slide 35. [1] ch.18 tr. 6 |
| Thuật toán có kiểm tra `PTE.Valid == False` → ngoại lệ | [1] | ch.18 tr. 9 (Hình 18.6) |
| Page-table length register (PTLR) | [2], [3] | [2] tr. 369. [3] slide 30, 35 |
| Paging không có external fragmentation | [2], [3], [1] | [2] tr. 360, 362. [3] slide 23. [1] ch.18 tr. 12 |
| Paging có internal fragmentation, trung bình nửa trang mỗi tiến trình | [2], [3] | [2] tr. 362–363. [3] slide 23, 28. (Ý "trung bình nửa trang" không có trong [1]; [1] ch.20 tr. 2 chỉ nói trang lớn làm tăng phân mảnh trong) |
| Page table quá lớn: 32-bit, trang 4 KB → 1 triệu entry × 4 byte = 4 MB/tiến trình | [2], [3], [1] | [2] mục 9.4.1 tr. 371. [3] slide 39. [1] ch.18 tr. 5, ch.20 tr. 1 |
| 64-bit, trang 4 KB: bảng có 2^52 mục | [3] | slide 43 |
| Bảng trang phần lớn là mục invalid vẫn chiếm chỗ (không gian địa chỉ thưa) | [1] | ch.20 tr. 4 |
| Trang lớn hơn làm bảng nhỏ lại (4 MB → 1 MB với trang 16 KB) nhưng tăng phân mảnh trong | [1] | ch.20 tr. 1–2 |
| Ví dụ thời gian truy cập hiệu dụng khi có TLB (80% trúng: 12 ns) | [3] | slide 34 |
| Hướng khắc phục: bảng phân cấp, bảng băm, bảng nghịch đảo | [2], [3] | [2] mục 9.4.1–9.4.3 tr. 371–375. [3] slide 39–47 |
| Chia sẻ trang chứa mã không tự sửa (reentrant) | [2], [3] | [2] mục 9.3.4 tr. 369–370. [3] slide 37 |
| Ví dụ chia sẻ: libc 2 MB, 40 tiến trình cần 80 MB nếu không chia sẻ | [2] | tr. 370 (slide 37 không có ví dụ số này) |
| Bit bảo vệ đọc/ghi cho từng frame | [2], [3] | [2] tr. 368. [3] slide 35 |
| Base/bounds: `PA = LA + base`; kiểm tra giới hạn | [1] | ch.15 tr. 6–7 |
| Base/bounds: một cặp thanh ghi trên chip cho mỗi CPU, lưu và nạp lại giá trị khi chuyển ngữ cảnh | [1] | ch.15 tr. 7, 10 |
| Base/bounds có thể gây phân mảnh trong (khoảng trống giữa stack và heap) | [1] | ch.15 tr. 13 |
| Segmentation: chia sẻ mã bằng bit bảo vệ cho từng segment | [1] | ch.16 tr. 7 |
| Segmentation: mỗi segment có cặp base/bounds riêng, tránh lãng phí khoảng trống giữa stack và heap | [1] | ch.16 tr. 1–3 |
| Bảng trang cho mỗi tiến trình một không gian địa chỉ riêng; trang là khối 4096 (2^12) byte; 12 bit thấp của địa chỉ ảo được chép nguyên sang địa chỉ vật lý (offset) | [4] | ch.3 mục 3.1, tr. 31 |
| Bit `PTE_V` cho biết PTE có hiệu lực; không đặt thì truy cập gây exception | [4] | ch.3, tr. 33 |
| Giới hạn của bảng trang một mảng phẳng: Sv39 có 2^27 PTE nên xv6 dùng cây ba cấp để tiết kiệm bộ nhớ; nhược điểm là CPU phải đọc ba PTE cho mỗi lần dịch, nên có TLB | [4] | ch.3 mục 3.1, tr. 31–32 |

File trích 19 trang giáo trình [2] (351, 353–354, 357, 359–363, 365–366, 368–375): [references/evidence/Silberschatz-OSC10-ch9-trang-duoc-trich.pdf](references/evidence/Silberschatz-OSC10-ch9-trang-duoc-trich.pdf).

## Tình trạng phần việc của Đăng (đối chiếu RESEARCH_PLAN.md)

| Tuần | Việc trong kế hoạch | Sản phẩm |
|---|---|---|
| 1 | Tìm slide học phần, ít nhất 1 giáo trình, tổng ≥ 4 nguồn có đủ thông tin trích dẫn | Danh mục [1]–[4] ở trên |
| 1 | Nháp cơ sở lý thuyết: logical/physical address, page, frame, page table, valid/invalid | [theory.md](theory.md) mục 2.1–2.5 |
| 1 | Ghi nguồn cho mọi công thức, hình, nội dung mượn | Trích dẫn `[số, tr. x]` trong mọi file; công thức `⌊LA/P⌋`, `LA mod P` ghi rõ là cách viết tương đương do nhóm suy ra |
| 2 | Giải thích cơ chế dịch theo từng bước | [theory.md](theory.md) mục 2.3–2.4 |
| 2 | Sơ đồ bảng trang một cấp (tự vẽ hoặc ghi nguồn) | [figures/page-table-single-level.svg](figures/page-table-single-level.svg) (nhóm tự vẽ) |
| 2 | Nháp giới hạn của mô hình một cấp | [limitations.md](limitations.md) phần A, B |
| 3 | So sánh với base/limit theo ≥ 3 tiêu chí | [comparison.md](comparison.md) (5 tiêu chí) |
| 3 | Ưu điểm, hạn chế và giả định của mô hình một cấp | [limitations.md](limitations.md) |
| 3 | Rà soát nguồn cho bảng so sánh và nhận định kỹ thuật | Đã đối chiếu từng ô với trang nguồn |
| 4 | Kiểm tra ≥ 4 nguồn gồm slide học phần và giáo trình | [2] giáo trình, [3] slide học phần, [1], [4] |
| 4 | Rà soát trích dẫn công thức, hình, bảng, code | Đã đối chiếu từng trích dẫn với trang nguồn (kiểm tra tự động theo từ khóa và kiểm tra độc lập từng câu, 23/11/2026) |
| 4 | Review chéo giải thuật, thuật ngữ, giải thích kết quả | [review-dang.md](review-dang.md) |

Còn lại cho báo cáo (không phải file trong repo):

- Lý đưa các phần trên vào báo cáo PDF và đánh lại số tài liệu, số hình, số bảng theo chương.
- Khai báo AI trong báo cáo: Claude Code hỗ trợ tìm đoạn, đối chiếu số trang và soạn nháp. Nội dung kỹ thuật do Đăng đối chiếu lại và chịu trách nhiệm.
- Nam xác nhận phần đóng góp của Đăng trong RESEARCH_PLAN.md.
