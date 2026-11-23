# Research Project Plan — Paging and Page-Table Address Translation

> **Học phần:** Hệ điều hành — Main Memory / Virtual Memory  
> **Quy mô:** 5 thành viên  
> **Khung kế hoạch:** 4 tuần theo tiến độ đề bài  
> **Đề gốc:** `2627_0101_Research_Requirement.pdf`

## 1. Thành viên và trách nhiệm

| Thành viên | Vai trò chính | Phần việc chịu trách nhiệm |
|---|---|---|
| **Nam** | Điều phối & tích hợp | Phạm vi, giả định, kiến trúc mô hình, review, tích hợp, kết luận |
| **Đăng** | Nghiên cứu lý thuyết | Paging, page table một cấp, valid/invalid, nguồn tham khảo, so sánh |
| **Minh** | Giải thuật & mô phỏng | Pseudocode, script, input/output, trace, độ phức tạp |
| **Sơn** | Kiểm thử & kiểm chứng | Test cases, expected result độc lập, actual result, pass/fail, bằng chứng |
| **Lý** | Báo cáo & trình bày | Bố cục PDF, biên tập, README, slide/video, trích dẫn |

## 2. Phạm vi và tiêu chí kỹ thuật chung

- [ ] Dùng **page table một cấp**, **page size cố định**, có **valid/invalid bit**.
- [ ] Chọn page size theo byte, ưu tiên lũy thừa của 2 (ví dụ 4, 8, 16, 1024); không thay đổi trong một bộ test.
- [ ] Quy định rõ cách đánh số page/frame, đơn vị, miền địa chỉ và các giả định.
- [ ] Dịch logical address (LA) theo `page = floor(LA / P)`, `offset = LA mod P`.
- [ ] Kiểm tra page có trong page table và entry hợp lệ trước khi lấy frame.
- [ ] Với entry hợp lệ, tính `physical address = frame × P + offset`.
- [ ] Với địa chỉ không hợp lệ, trả kết quả lỗi rõ ràng (`invalid`/`page fault` theo quy ước của nhóm).
- [ ] Không triển khai TLB, multi-level page table, page replacement, frame allocation, working set, thrashing, driver hoặc GUI trong phạm vi chính.

**Ví dụ đối chiếu trong đề:** `P = 16`, `LA = 37` → `page = 2`, `offset = 5`; nếu page 2 ánh xạ tới frame 7 thì `PA = 117`.

---

## 3. Tuần 1 — Đặc tả, nguồn và thiết kế kiểm thử

### Nam — Điều phối và thiết kế
- [ ] Tạo bảng theo dõi công việc.
- [ ] Chốt hai câu hỏi nghiên cứu: quy trình dịch LA → PA và điều kiện địa chỉ không hợp lệ.
- [ ] Viết `docs/specification.md`: phạm vi, giả định, cách đánh số page/frame, định dạng input/output và mã lỗi.
- [ ] Chốt page size và mẫu page table với cả nhóm.
- [ ] Review specification cùng Minh và Sơn để bảo đảm code/test dùng chung hợp đồng dữ liệu.

### Đăng — Nền tảng học thuật
- [ ] Tìm và đọc tài liệu/slide của học phần.
- [ ] Tìm ít nhất một giáo trình hoặc tài liệu học thuật về hệ điều hành.
- [ ] Thu thập tổng cộng ít nhất **4 nguồn phù hợp**, ghi đủ thông tin trích dẫn.
- [ ] Viết nháp cơ sở lý thuyết: logical/physical address, page, frame, page table, valid/invalid bit.
- [ ] Ghi nguồn cho mọi công thức, hình hoặc nội dung sử dụng từ tài liệu khác.

### Minh — Thiết kế mô phỏng
- [ ] Đề xuất cấu trúc page table và dữ liệu đầu vào.
- [ ] Định nghĩa output thành công, output lỗi và từng dòng trace.
- [ ] Phác thảo các bước thuật toán trước khi code.
- [ ] Xác nhận cùng Sơn cách tách code chính khỏi phương pháp tính expected result.

### Sơn — Thiết kế kiểm chứng
- [ ] Lập ma trận tối thiểu 8 trường hợp test theo đề.
- [ ] Thiết kế **cách tính expected result độc lập** (tính tay hoặc bảng tính/script ngắn, không sao chép logic chương trình chính).
- [ ] Chốt định dạng lưu `input`, `expected`, `actual`, `pass/fail` và trace.
- [ ] Chuẩn bị mẫu bằng chứng tính độc lập cho ít nhất 3 trường hợp.

### Lý — Khung tài liệu
- [ ] Tạo outline báo cáo 6–10 trang nội dung chính.
- [ ] Tạo mẫu bảng thuật ngữ, bảng test, bảng trích dẫn và danh mục hình.
- [ ] Tạo khung README và slide trình bày ngắn.
- [ ] Thống nhất quy tắc định dạng, tên file và cách trích dẫn với Đăng.

**Đầu ra tuần 1:** `docs/specification.md`, `docs/references.md`, outline báo cáo, test matrix bản nháp, thiết kế independent verification.

---

## 4. Tuần 2 — Giải thuật, mô phỏng và trace mẫu

### Nam
- [ ] Review pseudocode và các nhánh xử lý lỗi.
- [ ] Xác nhận chương trình tuân thủ specification tuần 1.
- [ ] Tích hợp và chạy thử một ví dụ thành công, một ví dụ lỗi.

### Đăng
- [ ] Hoàn thiện giải thích cơ chế dịch địa chỉ theo từng bước.
- [ ] Chuẩn bị sơ đồ page table một cấp (tự vẽ hoặc ghi nguồn).
- [ ] Viết nháp giới hạn của mô hình page table một cấp.

### Minh
- [ ] Viết pseudocode hoặc flowchart đầy đủ.
- [ ] Implement tách page number và offset.
- [ ] Implement kiểm tra page nằm trong page table và valid/invalid bit.
- [ ] Implement lấy frame, tính physical address và trả lỗi khi không hợp lệ.
- [ ] Xuất trace từng bước cho mỗi lần dịch.
- [ ] Viết phần phân tích độ phức tạp của một lần dịch, nêu rõ giả định về thao tác tra cứu.

### Sơn
- [ ] Chạy smoke test trên mô phỏng ban đầu.
- [ ] Kiểm tra ví dụ `P=16, LA=37, page 2 → frame 7, PA=117`.
- [ ] Ghi nhận lỗi và tạo issue tái hiện được.
- [ ] Chọn ít nhất 3 trường hợp để trình bày trace chi tiết, có hợp lệ và không hợp lệ.

### Lý
- [ ] Viết phần câu hỏi nghiên cứu, phạm vi, mô hình và giả định.
- [ ] Biên tập phần lý thuyết do Đăng cung cấp.
- [ ] Đưa pseudocode/flowchart và trace mẫu vào báo cáo nháp.
- [ ] Chuẩn bị slide giải thích một lần dịch LA → PA.

**Đầu ra tuần 2:** `src/` chạy được, pseudocode/flowchart, trace mẫu, báo cáo nháp phần lý thuyết và mô hình.

---

## 5. Tuần 3 — Kiểm thử, kiểm chứng độc lập và phân tích

### Nam
- [ ] Review tính nhất quán giữa specification, code và bộ test.
- [ ] Kiểm tra cách phân biệt lỗi page ngoài bảng với entry invalid theo quy ước đã công bố.
- [ ] Điều phối sửa lỗi và chạy regression test.

### Đăng
- [ ] So sánh paging với **segmentation hoặc base/limit relocation** theo ít nhất 3 tiêu chí.
- [ ] Viết phần ưu điểm, hạn chế và giả định của mô hình một cấp.
- [ ] Rà soát nguồn cho bảng so sánh và các nhận định kỹ thuật.

### Minh
- [ ] Hoàn thiện trace và xử lý các trường hợp biên.
- [ ] Tạo script chạy batch test, xuất actual result.
- [ ] Sửa lỗi được Sơn ghi nhận, bảo đảm chạy lại được trên dữ liệu lưu trong repo.
- [ ] Hoàn thiện phân tích độ phức tạp.

### Sơn
- [ ] Kiểm thử ít nhất 3 địa chỉ hợp lệ thuộc 3 page khác nhau.
- [ ] Kiểm thử offset = 0.
- [ ] Kiểm thử offset = P − 1.
- [ ] Kiểm thử page number ngoài page table.
- [ ] Kiểm thử page table entry invalid.
- [ ] Kiểm thử ít nhất 1 trường hợp biên tự chọn.
- [ ] Lưu input, expected result, actual result và pass/fail cho **từng test**.
- [ ] Ghi trace chi tiết cho ít nhất 3 trường hợp, bao gồm hợp lệ và không hợp lệ.
- [ ] Đối chiếu **ít nhất 3 trường hợp** bằng phương pháp tính độc lập, lưu bằng chứng có thể kiểm tra.

### Lý
- [ ] Tổng hợp bảng kết quả test và trace vào báo cáo.
- [ ] Viết phần kiểm chứng, phân tích kết quả, so sánh và giới hạn.
- [ ] Đảm bảo hình/bảng có chú thích và nguồn khi cần.
- [ ] Cập nhật slide với kết quả test và bằng chứng.

**Đầu ra tuần 3:** `tests/`, `data/expected_results.*`, `data/actual_results.*`, `data/traces/`, `verification/`, bảng so sánh và phân tích.

---

## 6. Tuần 4 — Hồ sơ nộp, rà soát và trình bày

### Nam
- [ ] Review toàn bộ yêu cầu trong PDF đề bài.
- [ ] Kiểm tra code, report và kết quả có nhất quán.
- [ ] Tổ chức review chéo và chạy thử quy trình tái hiện từ đầu.
- [ ] Tổng hợp contribution statement dựa trên đóng góp thực tế của từng người.
- [ ] Xác nhận bộ hồ sơ cuối cùng trước khi nộp.

### Đăng
- [ ] Kiểm tra tối thiểu 4 nguồn phù hợp, gồm slide/tài liệu học phần và giáo trình/tài liệu học thuật.
- [ ] Rà soát trích dẫn công thức, hình, bảng, code và nội dung mượn nguồn.
- [ ] Review chéo phần giải thuật, thuật ngữ và giải thích kết quả.

### Minh
- [ ] Làm sạch code và thêm hướng dẫn tham số cần thiết.
- [ ] Kiểm tra chạy được từ môi trường sạch theo README.
- [ ] Xuất lại actual results và traces từ bản code cuối.
- [ ] Hỗ trợ demo giải thuật và giải thích độ phức tạp.

### Sơn
- [ ] Chạy lại toàn bộ test trên bản cuối và lưu kết quả.
- [ ] Xác nhận từng expected/actual/pass-fail.
- [ ] Kiểm tra bằng chứng độc lập không phụ thuộc vào logic code chính.
- [ ] Review chéo demo và các trường hợp invalid.

### Lý
- [ ] Hoàn thiện PDF **6–10 trang nội dung chính** với đầy đủ phần bắt buộc.
- [ ] Hoàn thiện README: cách chạy và cách tái tạo kết quả.
- [ ] Hoàn thiện slide **hoặc** video trình bày ngắn.
- [ ] Bổ sung bảng phân công và contribution statement đã xác nhận.
- [ ] Khai báo công cụ AI và mục đích sử dụng nếu có.
- [ ] Xuất PDF và kiểm tra hiển thị, trích dẫn, tên file.

**Đầu ra tuần 4:** báo cáo PDF, source/script, README, input/page table/expected/actual/trace, bằng chứng độc lập, slide/video, phân công & contribution statement.

---

## 7. Ma trận kiểm thử tối thiểu

| ID | Trường hợp | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| T01 | Địa chỉ hợp lệ ở page A | Chưa tính | Chưa chạy | ☐ |
| T02 | Địa chỉ hợp lệ ở page B (khác A) | Chưa tính | Chưa chạy | ☐ |
| T03 | Địa chỉ hợp lệ ở page C (khác A, B) | Chưa tính | Chưa chạy | ☐ |
| T04 | Offset = 0 | Chưa tính | Chưa chạy | ☐ |
| T05 | Offset = P − 1 | Chưa tính | Chưa chạy | ☐ |
| T06 | Page number ngoài page table | Chưa tính | Chưa chạy | ☐ |
| T07 | Page table entry invalid | Chưa tính | Chưa chạy | ☐ |
| T08 | Trường hợp biên do nhóm chọn | Chưa tính | Chưa chạy | ☐ |

> Điền dữ liệu cụ thể sau khi thống nhất page table. Không đánh dấu PASS nếu chưa có actual result và đối chiếu.

## 8. Checklist nghiệm thu cuối

- [ ] Trả lời rõ 2 câu hỏi research.
- [ ] Giải thích mô hình một cấp, giả định, đơn vị, đánh số page/frame và công thức.
- [ ] Có pseudocode hoặc flowchart.
- [ ] Có mô phỏng chạy được, input/output/trace rõ ràng.
- [ ] Có phân tích độ phức tạp.
- [ ] Có so sánh với segmentation hoặc base/limit theo ít nhất 3 tiêu chí.
- [ ] Có giới hạn mô hình một cấp.
- [ ] Có ít nhất 8 test đúng các nhóm yêu cầu.
- [ ] Có input, expected, actual, pass/fail cho từng test.
- [ ] Có ít nhất 3 trace chi tiết, gồm hợp lệ và không hợp lệ.
- [ ] Có ít nhất 3 trường hợp kiểm chứng bằng cách tính độc lập và bằng chứng lưu lại.
- [ ] Có báo cáo PDF 6–10 trang nội dung chính, đủ các mục theo đề.
- [ ] Có README và dữ liệu tái hiện.
- [ ] Có slide hoặc video ngắn.
- [ ] Có ít nhất 4 nguồn phù hợp và trích dẫn thống nhất.
- [ ] Có bảng phân công và contribution statement đúng thực tế.
- [ ] Có khai báo sử dụng AI nếu có.
- [ ] Cả 5 thành viên đều có thể giải thích mô hình, giải thuật và phần việc của mình.

## 9. Đóng góp thực tế

| Thành viên | Công việc thực tế đã hoàn thành | Minh chứng (commit/PR/file) | Xác nhận |
|---|---|---|---|
| Nam | _Chưa cập nhật_ | _Chưa cập nhật_ | ☐ |
| Đăng | _Chưa cập nhật_ | _Chưa cập nhật_ | ☐ |
| Minh | _Chưa cập nhật_ | _Chưa cập nhật_ | ☐ |
| Sơn | _Chưa cập nhật_ | _Chưa cập nhật_ | ☐ |
| Lý | _Chưa cập nhật_ | _Chưa cập nhật_ | ☐ |

---

Ghi ngày thực hiện và đóng góp theo tiến độ thực tế.
