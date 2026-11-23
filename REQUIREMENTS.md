# REQUIREMENTS — Paging and Page-Table Address Translation

> **Nguồn sự thật (source of truth):** `2627_0101_Research_Requirement.pdf` (4 trang).  
> **Mục đích:** Context ngắn gọn để AI/nhóm đọc trước khi code, test, viết báo cáo hoặc review.  
> **Trạng thái:** Đây là bản tóm tắt yêu cầu, **không phải** bằng chứng đã hoàn thành. Nếu có xung đột, ưu tiên PDF gốc.

## 1. Bối cảnh và mục tiêu (trang 1)

- Chủ đề: **Paging và page-table address translation**, thuộc **Main Memory / Virtual Memory**.
- Quy mô: **5 sinh viên/nhóm**; thời gian trong đề: **4 tuần**.
- Sản phẩm trọng tâm: **báo cáo research + mô phỏng/giải thuật + bằng chứng kiểm chứng**.
- Câu hỏi phải trả lời:
  1. Với **page table một cấp**, logical address được dịch sang physical address thế nào?
  2. Khi nào địa chỉ được xem là không hợp lệ?

## 2. Phạm vi bắt buộc (trang 1–2)

- **Single-level page table**, **page size cố định**, có **valid/invalid bit**.
- Page size `P` đo bằng **byte**, nên chọn lũy thừa của 2 (ví dụ **4, 8, 16, 1024** byte); **không thay đổi P trong cùng một bộ test**.
- Công thức:
  - `page_number = floor(logical_address / P)`
  - `offset = logical_address mod P`
  - Nếu page entry hợp lệ: `physical_address = frame_number * P + offset`
- Ví dụ từ đề: `P=16`, `LA=37` → `page=2`, `offset=5`; page 2 → frame 7 ⇒ `PA=117`.
- Giải thuật phải thực hiện đủ **6 bước**:
  1. Tách page number và offset.
  2. Kiểm tra page number có trong page table không.
  3. Kiểm tra valid/invalid bit.
  4. Lấy frame number nếu entry hợp lệ.
  5. Tính physical address.
  6. Trả kết quả hoặc thông báo **invalid/page fault**.
- **Không yêu cầu:** TLB, multi-level page table, page replacement, frame allocation, working set, thrashing, driver, GUI. Mở rộng (nếu có) phải tách riêng, không làm mất trọng tâm.

## 3. Yêu cầu thực hiện (trang 2)

- [ ] Nêu rõ **giả định, đơn vị đo, cách đánh số page/frame, công thức**.
- [ ] Có **pseudocode hoặc flowchart**.
- [ ] Có **mô phỏng/script** với **input, output, trace rõ ràng**.
- [ ] Phân tích **độ phức tạp của một lần dịch địa chỉ**.
- [ ] So sánh ngắn gọn với **segmentation hoặc base/limit relocation** theo **ít nhất 3 tiêu chí**.
- [ ] Nêu **giới hạn** của mô hình page table một cấp.

## 4. Kiểm thử và kiểm chứng (trang 2–3)

- [ ] **Ít nhất 8 test case**, bao phủ:
  - **3 địa chỉ hợp lệ thuộc các page khác nhau**;
  - **offset = 0**;
  - **offset = P − 1**;
  - **page number ngoài page table**;
  - **page table entry không hợp lệ**;
  - **1 trường hợp biên do nhóm tự chọn**.
- [ ] **Mỗi test** có: `input`, `expected result`, `actual result`, `pass/fail`.
- [ ] **Ít nhất 3 trace chi tiết**, trong đó có **ít nhất 1 hợp lệ và 1 không hợp lệ**.
- [ ] Có **cách tính expected result độc lập với chương trình chính**: tính tay, bảng tính hoặc script rất ngắn; **không sao chép nguyên logic chương trình chính**.
- [ ] Đối chiếu độc lập cho **ít nhất 3 trường hợp**.
- Ví dụ expected độc lập trong đề: `floor(37/16)=2`, `37 mod 16=5`, `7*16+5=117`; so sánh `actual` với `117`.

## 5. Hồ sơ phải nộp (trang 3)

- [ ] **Báo cáo PDF khoảng 6–10 trang nội dung chính**.
- [ ] **Mã nguồn / notebook / script** mô phỏng.
- [ ] **README** hướng dẫn chạy và tái tạo kết quả.
- [ ] **File input, page table, expected result, actual result và trace**.
- [ ] **Bằng chứng kiểm chứng độc lập**.
- [ ] **Slide hoặc video trình bày ngắn**.
- [ ] **Bảng phân công + contribution statement** của từng thành viên.

### Các phần bắt buộc trong báo cáo

1. Câu hỏi và phạm vi.
2. Cơ sở lý thuyết.
3. Mô hình và giả định.
4. Giải thuật.
5. Kết quả/trace.
6. Kiểm chứng.
7. Phân tích.
8. Giới hạn.
9. Kết luận.
10. Tài liệu tham khảo.

## 6. Nguồn và liêm chính học thuật (trang 3–4)

- [ ] **Tối thiểu 4 nguồn phù hợp**, bắt buộc có **tài liệu/slide học phần** và **ít nhất 1 giáo trình hoặc tài liệu học thuật về Hệ điều hành**.
- [ ] Trích dẫn **thống nhất** cho công thức, hình, bảng, mã nguồn và nội dung không do nhóm tự tạo.
- [ ] **AI không được dùng làm nguồn kỹ thuật chính**.
- [ ] Nếu dùng AI, **khai báo công cụ và mục đích sử dụng**.
- [ ] **Mọi thành viên** hiểu mô hình, giải thuật và phần việc của mình.
- [ ] Không trình bày số liệu/hình ảnh **không có cách tái hiện**; nhóm chịu trách nhiệm kiểm tra và giải thích toàn bộ bài.
- **Điều kiện hoàn thành theo đề:** mô phỏng/giải thuật **chạy được**, có **expected**, **actual** và **bằng chứng kiểm chứng độc lập**.

## 7. Tiến độ 4 tuần trong đề (trang 3)

| Tuần | Nội dung |
|---|---|
| 1 | Chốt câu hỏi, phạm vi, giả định, nguồn và thiết kế cách tính độc lập để kiểm tra kết quả. |
| 2 | Hoàn thành pseudocode, mô phỏng ban đầu và trace mẫu. |
| 3 | Hoàn thiện bộ test, kiểm chứng độc lập và phân tích kết quả. |
| 4 | Hoàn thiện báo cáo, README, slide/video, review chéo và chuẩn bị trình bày. |

> **Lưu ý:** Đây là tiến độ **đề nghị** của thầy, không phải bằng chứng nhóm đã làm đủ bốn tuần.

## 8. Quy ước nội bộ của nhóm — KHÔNG phải yêu cầu từ thầy

- Nhóm: **Nam, Đăng, Minh, Sơn, Lý**. Phân công chi tiết: xem `RESEARCH_PLAN.md`.
- Nhóm muốn triển khai trong **24 giờ** nhưng **tổ chức đầu việc theo 4 giai đoạn/tuần** như đề. Không ghi sai ngày làm hoặc đóng góp thực tế.
- Những thứ **chưa được đề quy định** và nhóm phải tự chốt: ngôn ngữ lập trình, `P` cụ thể, cấu trúc input/output, page table cụ thể, cách biểu diễn lỗi, cách đánh số page/frame, test case biên, format trace, cấu trúc repo, chuẩn trích dẫn.
- Không tự suy diễn rằng phải có GUI, TLB, page replacement hoặc các phần mở rộng khác.

## 9. Hướng dẫn cho AI khi làm việc với repo

1. **Đọc file này trước**, sau đó đọc `RESEARCH_PLAN.md` để biết người phụ trách và checklist.
2. **Phân biệt**: yêu cầu gốc (mục 1–7) và quyết định nội bộ (mục 8).
3. Không tự tuyên bố test PASS, hoàn thành, có bằng chứng hoặc trích dẫn khi chưa chạy/kiểm tra thực tế.
4. Nếu thiếu quyết định kỹ thuật, nêu giả định rõ ràng và xin nhóm xác nhận khi cần.
5. Giữ khả năng **tái hiện**: lệnh chạy, dữ liệu input, expected, actual, trace, cách kiểm chứng độc lập.
6. Khi viết báo cáo, dùng nguồn học thuật thực tế; không trích AI như nguồn kỹ thuật chính.
7. Khi review, kiểm tra từng checkbox ở mục 3–6, ưu tiên các điều kiện nghiệm thu bắt buộc.
