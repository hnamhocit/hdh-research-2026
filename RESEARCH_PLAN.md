# Research Project Plan — Paging and Page-Table Address Translation

> **Học phần:** Hệ điều hành — Main Memory / Virtual Memory  
> **Quy mô:** 5 thành viên  
> **Khung kế hoạch:** 4 tuần theo tiến độ đề bài  
> **Đề gốc:** [2627_0101_Research_Requirement.pdf](docs/2627_0101_Research_Requirement.pdf)

## 1. Thành viên và trách nhiệm

| Thành viên | Vai trò chính | Phần việc chịu trách nhiệm |
|---|---|---|
| **Nam** | Điều phối & tích hợp | Phạm vi, giả định, kiến trúc mô hình, review, tích hợp, kết luận |
| **Đăng** | Nghiên cứu lý thuyết | Paging, page table một cấp, valid/invalid, nguồn tham khảo, so sánh |
| **Minh** | Giải thuật & mô phỏng | Pseudocode, script, input/output, trace, độ phức tạp |
| **Sơn** | Kiểm thử & kiểm chứng | Test cases, expected result độc lập, actual result, pass/fail, bằng chứng |
| **Ly** | Báo cáo & trình bày | Bố cục PDF, biên tập, README, slide/video, trích dẫn |

## 2. Phạm vi và tiêu chí kỹ thuật chung

- [x] Dùng **page table một cấp**, **page size cố định**, có **valid/invalid bit**.
- [x] Chọn page size theo byte, ưu tiên lũy thừa của 2 (ví dụ 4, 8, 16, 1024); không thay đổi trong một bộ test.
- [x] Quy định rõ cách đánh số page/frame, đơn vị, miền địa chỉ và các giả định.
- [x] Dịch logical address (LA) theo `page = floor(LA / P)`, `offset = LA mod P`.
- [x] Kiểm tra page có trong page table và entry hợp lệ trước khi lấy frame.
- [x] Với entry hợp lệ, tính `physical address = frame × P + offset`.
- [x] Với địa chỉ không hợp lệ, trả kết quả lỗi rõ ràng (`invalid`/`page fault` theo quy ước của nhóm).
- [x] Không triển khai TLB, multi-level page table, page replacement, frame allocation, working set, thrashing, driver hoặc GUI trong phạm vi chính.

**Ví dụ đối chiếu trong đề:** `P = 16`, `LA = 37` → `page = 2`, `offset = 5`; nếu page 2 ánh xạ tới frame 7 thì `PA = 117`.

---

## 3. Tuần 1 — Đặc tả, nguồn và thiết kế kiểm thử

### Nam — Điều phối và thiết kế

[Xem bảng theo dõi và checklist tích hợp của Nam](docs/integration-review.md).

- [x] Tạo bảng theo dõi công việc.
- [x] Chốt hai câu hỏi nghiên cứu: quy trình dịch LA → PA và điều kiện địa chỉ không hợp lệ.
- [x] Viết `docs/specification.md`: phạm vi, giả định, cách đánh số page/frame, định dạng input/output và mã lỗi.
- [ ] Chốt page size và mẫu page table với cả nhóm.
- [ ] Review specification cùng Minh và Sơn để bảo đảm code/test dùng chung hợp đồng dữ liệu.

### Đăng — Nền tảng học thuật
- [x] Tìm và đọc tài liệu/slide của học phần.
- [x] Tìm ít nhất một giáo trình hoặc tài liệu học thuật về hệ điều hành.
- [x] Thu thập tổng cộng ít nhất **4 nguồn phù hợp**, ghi đủ thông tin trích dẫn.
- [x] Viết nháp cơ sở lý thuyết: logical/physical address, page, frame, page table, valid/invalid bit.
- [x] Ghi nguồn cho mọi công thức, hình hoặc nội dung sử dụng từ tài liệu khác.

### Minh — Thiết kế mô phỏng
- [x] Đề xuất cấu trúc page table và dữ liệu đầu vào.
- [x] Định nghĩa output thành công, output lỗi và từng dòng trace.
- [x] Phác thảo các bước thuật toán trước khi code.
- [ ] Xác nhận cùng Sơn cách tách code chính khỏi phương pháp tính expected result.

### Sơn — Thiết kế kiểm chứng
- [x] Lập ma trận tối thiểu 8 trường hợp test theo đề.
- [x] Thiết kế **cách tính expected result độc lập** (tính tay hoặc bảng tính/script ngắn, không sao chép logic chương trình chính).
- [x] Chốt định dạng lưu `input`, `expected`, `actual`, `pass/fail` và trace.
- [x] Chuẩn bị mẫu bằng chứng tính độc lập cho ít nhất 3 trường hợp.

### Ly — Khung tài liệu
- [x] Tạo outline báo cáo 6–10 trang nội dung chính.
- [ ] Tạo mẫu bảng thuật ngữ, bảng test, bảng trích dẫn và danh mục hình.
- [x] Tạo khung README và slide trình bày ngắn.
- [ ] Thống nhất quy tắc định dạng, tên file và cách trích dẫn với Đăng.

**Đầu ra tuần 1:** `docs/specification.md`, `docs/references.md`, outline báo cáo, test matrix bản nháp, thiết kế independent verification.

---

## 4. Tuần 2 — Giải thuật, mô phỏng và trace mẫu

### Nam

[Xem minh chứng chạy tích hợp và regression](docs/integration-review.md#ca-tích-hợp).

- [x] Review pseudocode và các nhánh xử lý lỗi.
- [x] Xác nhận chương trình tuân thủ specification tuần 1.
- [x] Tích hợp và chạy thử một ví dụ thành công, một ví dụ lỗi.

### Đăng
- [x] Hoàn thiện giải thích cơ chế dịch địa chỉ theo từng bước.
- [x] Chuẩn bị sơ đồ page table một cấp (tự vẽ hoặc ghi nguồn).
- [x] Viết nháp giới hạn của mô hình page table một cấp.

### Minh
- [x] Viết pseudocode hoặc flowchart đầy đủ.
- [x] Implement tách page number và offset.
- [x] Implement kiểm tra page nằm trong page table và valid/invalid bit.
- [x] Implement lấy frame, tính physical address và trả lỗi khi không hợp lệ.
- [x] Xuất trace từng bước cho mỗi lần dịch.
- [x] Viết phần phân tích độ phức tạp của một lần dịch, nêu rõ giả định về thao tác tra cứu.

### Sơn
- [x] Chạy smoke test trên mô phỏng ban đầu.
- [x] Kiểm tra ví dụ `P=16, LA=37, page 2 → frame 7, PA=117`.
- Nếu phát hiện lỗi, ghi nhận và tạo issue tái hiện được.
- [x] Chọn ít nhất 3 trường hợp để trình bày trace chi tiết, có hợp lệ và không hợp lệ.

### Ly
- [x] Viết phần câu hỏi nghiên cứu, phạm vi, mô hình và giả định.
- [x] Biên tập phần lý thuyết do Đăng cung cấp.
- [x] Đưa pseudocode/flowchart và trace mẫu vào báo cáo nháp.
- [x] Chuẩn bị slide giải thích một lần dịch LA → PA.

**Đầu ra tuần 2:** `src/` chạy được, pseudocode/flowchart, trace mẫu, báo cáo nháp phần lý thuyết và mô hình.

---

## 5. Tuần 3 — Kiểm thử, kiểm chứng độc lập và phân tích

### Nam

[Xem minh chứng chạy tích hợp và regression](docs/integration-review.md#ca-tích-hợp).

- [x] Review tính nhất quán giữa specification, code và bộ test.
- [x] Kiểm tra cách phân biệt lỗi page ngoài bảng với entry invalid theo quy ước đã công bố.
- [x] Điều phối sửa lỗi và chạy regression test.

### Đăng
- [x] So sánh paging với **segmentation hoặc base/limit relocation** theo ít nhất 3 tiêu chí.
- [x] Viết phần ưu điểm, hạn chế và giả định của mô hình một cấp.
- [x] Rà soát nguồn cho bảng so sánh và các nhận định kỹ thuật.

### Minh
- [x] Hoàn thiện trace và xử lý các trường hợp biên.
- [x] Tạo script chạy batch test, xuất actual result.
- Nếu Sơn ghi nhận lỗi, sửa và chạy lại trên dữ liệu lưu trong repo.
- [x] Hoàn thiện phân tích độ phức tạp.

### Sơn
- [x] Kiểm thử ít nhất 3 địa chỉ hợp lệ thuộc 3 page khác nhau.
- [x] Kiểm thử offset = 0.
- [x] Kiểm thử offset = P − 1.
- [x] Kiểm thử page number ngoài page table.
- [x] Kiểm thử page table entry invalid.
- [x] Kiểm thử ít nhất 1 trường hợp biên tự chọn.
- [x] Lưu input, expected result, actual result và pass/fail cho **từng test**.
- [x] Ghi trace chi tiết cho ít nhất 3 trường hợp, bao gồm hợp lệ và không hợp lệ.
- [x] Đối chiếu **ít nhất 3 trường hợp** bằng phương pháp tính độc lập, lưu bằng chứng có thể kiểm tra.

### Ly
- [x] Tổng hợp bảng kết quả test và trace vào báo cáo.
- [x] Viết phần kiểm chứng, phân tích kết quả, so sánh và giới hạn.
- [x] Đảm bảo hình/bảng có chú thích và nguồn khi cần.
- [x] Cập nhật slide với kết quả test và bằng chứng.

**Đầu ra tuần 3:** `tests/`, `data/expected_results.*`, `data/actual_results.*`, `data/traces/`, `verification/`, bảng so sánh và phân tích.

---

## 6. Tuần 4 — Hồ sơ nộp, rà soát và trình bày

### Nam

[Xem kết quả rà soát tuần 4 và các mục chờ xác nhận](docs/integration-review.md#kết-quả-rà-soát-tuần-4).

- [x] Review toàn bộ yêu cầu trong PDF đề bài.
- [x] Kiểm tra code, report và kết quả có nhất quán.
  - [x] Đối chiếu code, đặc tả và kết quả tích hợp.
  - [x] Đối chiếu mô hình, thuật toán và bảng kết quả trong báo cáo PDF với code và dữ liệu tích hợp.
- [ ] Tổ chức review chéo và chạy thử quy trình tái hiện từ đầu.
  - [x] Chạy lại theo README từ thư mục tạm và đối chiếu file kết quả.
  - [ ] Tổ chức review chéo với các thành viên.
- [x] Tổng hợp contribution statement dựa trên đóng góp thực tế của từng người.
- [ ] Xác nhận bộ hồ sơ cuối cùng trước khi nộp.

### Đăng
- [x] Kiểm tra tối thiểu 4 nguồn phù hợp, gồm slide/tài liệu học phần và giáo trình/tài liệu học thuật.
- [x] Rà soát trích dẫn công thức, hình, bảng, code và nội dung mượn nguồn.
- [x] Review chéo phần giải thuật, thuật ngữ và giải thích kết quả.

### Minh
- [x] Làm sạch code và thêm hướng dẫn tham số cần thiết.
- [x] Kiểm tra chạy được từ môi trường sạch theo README.
- [x] Xuất lại actual results và traces từ bản code cuối.
- [ ] Hỗ trợ demo giải thuật và giải thích độ phức tạp.

### Sơn
- [x] Chạy lại toàn bộ test trên bản cuối và lưu kết quả.
- [x] Xác nhận từng expected/actual/pass-fail.
- [x] Kiểm tra bằng chứng độc lập không phụ thuộc vào logic code chính.
- [ ] Review chéo demo và các trường hợp invalid.

### Ly
- [x] Hoàn thiện PDF **6–10 trang nội dung chính** với đầy đủ phần bắt buộc.
- [x] Hoàn thiện README: cách chạy và cách tái tạo kết quả.
- [ ] Hoàn thiện slide **hoặc** video trình bày ngắn.
- [x] Bổ sung bảng phân công và contribution statement đã xác nhận.
- [ ] Khai báo công cụ AI và mục đích sử dụng nếu có.
- [x] Xuất PDF và kiểm tra hiển thị, trích dẫn, tên file.

**Đầu ra tuần 4:** báo cáo PDF, source/script, README, input/page table/expected/actual/trace, bằng chứng độc lập, slide/video, phân công & contribution statement.

---

## 7. Ma trận kiểm thử tối thiểu

| ID | Trường hợp | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| T01 | LA 37, hợp lệ ở page 2 | PA 117 | PA 117 | PASS |
| T02 | LA 51, hợp lệ ở page 3 | PA 3 | PA 3 | PASS |
| T03 | LA 5, hợp lệ ở page 0 | PA 53 | PA 53 | PASS |
| T04 | LA 48, offset = 0 | PA 0 | PA 0 | PASS |
| T05 | LA 63, offset = P − 1 | PA 15 | PA 15 | PASS |
| T06 | LA 64, page ngoài bảng | `PAGE_OUT_OF_RANGE` | `PAGE_OUT_OF_RANGE` | PASS |
| T07 | LA 16, entry invalid | `INVALID_ENTRY` | `INVALID_ENTRY` | PASS |
| T08 | LA −1, địa chỉ âm | `INVALID_ADDRESS` | `INVALID_ADDRESS` | PASS |

[Xem kết quả tích hợp](data/actual_results.json) và [đối chiếu theo dải byte](verification/byte-ranges.md).

## 8. Checklist nghiệm thu cuối

Đã đối chiếu với PDF đề gốc và chạy lại bộ test tích hợp (8/8 PASS). Báo cáo có 9 trang nội dung chính và phụ lục mô tả đóng góp của cả 5 thành viên. Đóng góp và phần trình bày của cả nhóm đã được xác nhận theo thông báo của Nam. Khai báo AI trong Phụ lục B cần đối chiếu với [nhật ký hỗ trợ](docs/integration-review.md#kết-luận-dự-thảo-cho-báo-cáo). Slide cần làm rõ số ca tính tay và số lần truy cập bộ nhớ khi thiếu TLB.

- [x] Trả lời rõ 2 câu hỏi research.
- [x] Giải thích mô hình một cấp, giả định, đơn vị, đánh số page/frame và công thức.
- [x] Có pseudocode hoặc flowchart.
- [x] Có mô phỏng chạy được, input/output/trace rõ ràng.
- [x] Có phân tích độ phức tạp.
- [x] Có so sánh với segmentation hoặc base/limit theo ít nhất 3 tiêu chí.
- [x] Có giới hạn mô hình một cấp.
- [x] Có ít nhất 8 test đúng các nhóm yêu cầu.
- [x] Có input, expected, actual, pass/fail cho từng test.
- [x] Có ít nhất 3 trace chi tiết, gồm hợp lệ và không hợp lệ.
- [x] Có ít nhất 3 trường hợp kiểm chứng bằng cách tính độc lập và bằng chứng lưu lại.
- [x] Có báo cáo PDF 6–10 trang nội dung chính, đủ các mục theo đề.
- [x] Có README và dữ liệu tái hiện.
- [x] Có slide hoặc video ngắn.
- [x] Có ít nhất 4 nguồn phù hợp và trích dẫn thống nhất.
- [x] Có bảng phân công và contribution statement đúng thực tế.
- [ ] Có khai báo sử dụng AI nếu có.
- [x] Cả 5 thành viên đều có thể giải thích mô hình, giải thuật và phần việc của mình.

## 9. Đóng góp thực tế

Bản đối chiếu theo lịch sử Git và hồ sơ hiện tại. Nam xác nhận đóng góp và phân công trình bày của cả 5 thành viên.

| Thành viên | Đóng góp có minh chứng | Phần trình bày | Xác nhận theo Nam |
|---|---|---|---|
| Nam | Đặc tả, dữ liệu tích hợp và rà soát kết quả. Có hỗ trợ từ Codex theo [nhật ký](docs/integration-review.md). Minh chứng: `811e624`, [đặc tả](docs/specification.md). | Slide 1–2 và phần kết luận ở slide 10: giới thiệu, hai câu hỏi nghiên cứu và kết luận. | ✓ |
| Đăng | Cơ sở lý thuyết, sơ đồ, nguồn, so sánh, giới hạn và review chéo. Minh chứng: `312fef0`, `7359a83`, `8478684`, `6016fac`. | Slide 3, phần so sánh ở slide 9 và phần giới hạn ở slide 10. | ✓ |
| Minh | Simulator, tương thích đầu vào tích hợp và phân tích độ phức tạp. Minh chứng: `974a686`, `8aab25f`, `9e16859`. | Slide 4–5 và phần độ phức tạp ở slide 9: giải thuật, mã lỗi và ví dụ dịch LA 37. | ✓ |
| Sơn | Ma trận kiểm thử, trace và bằng chứng đối chiếu độc lập. Minh chứng: `38c446b`, [ma trận kiểm thử](verification/test_matrix.md). | Slide 6–8: giải thích các trace, kết quả 8 ca và cách kiểm chứng độc lập. | ✓ |
| Ly | Biên tập báo cáo, README và slide. Minh chứng: `f509dee`, [báo cáo PDF](docs/Paging_Report.pdf). | Điều phối chuyển phần, phụ trách slide 11 và chuẩn bị bản PDF cuối. | ✓ |

Số slide theo [bản PDF trình bày hiện tại](presentation/Bài%20TT.pdf).

---

Ghi ngày thực hiện và đóng góp theo tiến độ thực tế.
