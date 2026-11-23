# Tài liệu tham khảo (Đăng)

Quy ước: ✅ đã mở file nguồn và đọc đúng đoạn được ghi. Mẫu trích dẫn theo hướng dẫn của trường (BM-BTL-07): `[số, tr. x-y]`, xếp ABC theo họ tác giả đầu.

## Danh mục (tiếng Anh)

[1] Arpaci-Dusseau R.H., Arpaci-Dusseau A.C. (2018). *Operating Systems: Three Easy Pieces*, Arpaci-Dusseau Books. Dùng Chương 15 "Mechanism: Address Translation", Chương 16 "Segmentation", Chương 18 "Paging: Introduction", Chương 20 "Paging: Smaller Tables". http://ostep.org ✅
- Các chương đã đọc đều ghi `[VERSION 1.10]` (chương 15 © 2008–23, chương 16, 18 © 2008–25). Preface ghi phát hành 8/2018 (v1.00) hoặc 7/2019 (v1.01). Ngày truy cập: 23/11/2026.
- Số trang bên dưới là số in trong file chương. Mục lục sách: chương 15 bắt đầu tr. 153, chương 16 tr. 169, chương 18 tr. 199, chương 20 tr. 231.
- Sách phát miễn phí theo từng chương tại http://ostep.org (không đưa file vào repo).

[2] Silberschatz A., Galvin P.B., Gagne G. (2018). *Operating System Concepts*, 10th ed., Wiley, Hoboken NJ. Chương 9 "Main Memory". ✅ (số trang là số in trên sách = số trang file PDF trừ 106)

[3] Silberschatz A., Galvin P.B., Gagne G. (2018). *Chapter 9: Main Memory* (slide `ch9.pptx`, học phần Hệ điều hành 012012500102, giảng viên Mai Ngọc Châu), Trường ĐH GTVT TP.HCM, https://courses.ut.edu.vn. ✅ (slide 25, 26, 33, 36 chỉ có tiêu đề và hình)

[4] Cox R., Kaashoek F., Morris R. (2024). *xv6: a simple, Unix-like teaching operating system*, rev4 (ngày 31/08/2024), MIT. Dùng Chương 3 "Page tables". https://pdos.csail.mit.edu/6.1810/2024/xv6/book-riscv-rev4.pdf ✅ (tải miễn phí từ trang môn học 6.1810 của MIT, đã đọc chương 3. Số trang in = số trang file PDF. Ngày truy cập 23/11/2026.)
- Lưu ý: xv6 dùng bảng trang **ba cấp** (RISC-V Sv39), không phải một cấp. Chỉ trích cho các ý chung (trang 4096 byte, offset 12 bit, bit valid) và cho phần giới hạn/mở rộng của mô hình một cấp. Không trích như mô hình một cấp.

## Bảng tra cứu: ý nào lấy từ đâu (chỉ các chỗ đã đọc)

| Ý trong báo cáo | Nguồn | Vị trí đã đọc |
|---|---|---|
| Logical address và physical address, MMU | [2] | mục 9.1.3, tr. 353–354 |
| Thanh ghi base và limit | [2] | mục 9.1.1, tr. 351 |
| Relocation register + limit register bảo vệ bộ nhớ, MMU cộng relocation vào logical address | [2], [3], [1] | [2] mục 9.2.1 tr. 357. [3] slide 17. [1] ch.15 tr. 5–7 |
| External fragmentation ở cấp phát liên tục | [2], [3], [1] | [2] mục 9.2.3 tr. 359. [3] slide 21. [1] ch.16 tr. 10 |
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
| Paging có internal fragmentation, trung bình nửa trang mỗi tiến trình | [2], [3] | [2] tr. 362–363. [3] slide 23, 28. [1] ch.20 tr. 2 (không phải ch.18, chương này không nói về ý này) |
| Page table quá lớn: 32-bit, trang 4 KB → 1 triệu entry × 4 byte = 4 MB/tiến trình | [2], [3] | [2] mục 9.4.1 tr. 371. [3] slide 39. [1] ch.18 tr. 5, ch.20 tr. 1 |
| 64-bit, trang 4 KB: bảng có 2^52 mục | [3] | slide 43 |
| Bảng trang phần lớn là mục invalid vẫn chiếm chỗ (không gian địa chỉ thưa) | [1] | ch.20 tr. 4 |
| Trang lớn hơn làm bảng nhỏ lại (4 MB → 1 MB với trang 16 KB) nhưng tăng phân mảnh trong | [1] | ch.20 tr. 1–2 |
| Ví dụ thời gian truy cập hiệu dụng khi có TLB (80% trúng: 12 ns) | [3] | slide 34 |
| Hướng khắc phục: bảng phân cấp, bảng băm, bảng nghịch đảo | [2], [3] | [2] mục 9.4.1–9.4.3 tr. 371–374. [3] slide 39–47 |
| Chia sẻ trang (libc 2 MB, 40 tiến trình: 80 MB nếu không chia sẻ) | [2], [3] | [2] mục 9.3.4 tr. 369–370. [3] slide 37 |
| Bit bảo vệ đọc/ghi cho từng frame | [2], [3] | [2] tr. 368. [3] slide 35 |
| Base/bounds: hai thanh ghi trên chip, phải đổi khi chuyển ngữ cảnh | [1] | ch.15 tr. 7, 10 |
| Base/bounds có thể gây phân mảnh trong (khoảng trống giữa stack và heap) | [1] | ch.15 tr. 13 |
| Segmentation: chia sẻ mã bằng bit bảo vệ cho từng segment | [1] | ch.16 tr. 7 |
| Segmentation: mỗi segment có cặp base/bounds riêng | [1] | ch.16 tr. 1–3 |
| Bảng trang cho mỗi tiến trình một không gian địa chỉ riêng; trang là khối 4096 (2^12) byte; 12 bit thấp của địa chỉ ảo được chép nguyên sang địa chỉ vật lý (offset) | [4] | ch.3 mục 3.1, tr. 31 |
| Bit `PTE_V` cho biết PTE có hiệu lực; không đặt thì truy cập gây exception | [4] | ch.3, tr. 33 |
| Giới hạn của bảng trang một mảng phẳng: Sv39 có 2^27 PTE nên xv6 dùng cây ba cấp để tiết kiệm bộ nhớ; nhược điểm là CPU phải đọc ba PTE cho mỗi lần dịch, nên có TLB | [4] | ch.3 mục 3.1, tr. 31–32 |

File trích 14 trang giáo trình [2] (351, 353–354, 357, 359–363, 365–366, 368–369, 371): [references/evidence/Silberschatz-OSC10-ch9-trang-duoc-trich.pdf](references/evidence/Silberschatz-OSC10-ch9-trang-duoc-trich.pdf).

## Còn lại

- [x] Nguồn [4] đã chốt là xv6 (MIT), đủ 4 nguồn có thể đọc và đối chiếu.
- [x] So sánh paging với base/limit: xem [comparison.md](comparison.md). Giáo trình [2] chỉ nhắc segmentation ở ví dụ Intel IA-32 (mục 9.6.1, tr. 379), nên nguồn chính cho segmentation là [1] chương 16.
- [x] Ưu điểm và giới hạn của mô hình một cấp: xem [limitations.md](limitations.md). Cơ sở lý thuyết: xem [theory.md](theory.md).
- [x] Sơ đồ bảng trang một cấp (nhóm tự vẽ): [figures/page-table-single-level.svg](figures/page-table-single-level.svg).
- [x] Review chéo giải thuật và thuật ngữ với phần của Minh: xem [review-dang.md](review-dang.md).
- [ ] Khai báo AI trong báo cáo: Claude Code hỗ trợ tìm đoạn và số trang trong nguồn. Nội dung kỹ thuật do Đăng đối chiếu lại.
