# Paging and Page-Table Address Translation

Đồ án Hệ điều hành về dịch địa chỉ logic sang địa chỉ vật lý bằng bảng trang một cấp.

- [Yêu cầu đồ án](REQUIREMENTS.md)
- [Tiến độ và phân công](RESEARCH_PLAN.md)
- [Tài liệu kỹ thuật tổng hợp](docs/TECHNICAL_DOC.md)

## Hồ sơ báo cáo và trình bày

- [Báo cáo nghiên cứu (PDF)](docs/Paging_Report.pdf)
- [Slide thuyết trình (PDF)](presentation/B%C3%A0i%20TT.pdf)

## Thành viên thực hiện

| Thành viên | Vai trò chính |
| :--- | :--- |
| **Nam** | Điều phối, đặc tả kỹ thuật và tích hợp |
| **Đăng** | Nghiên cứu lý thuyết, bảng so sánh và tài liệu tham khảo |
| **Minh** | Giải thuật, mã mô phỏng và phân tích độ phức tạp |
| **Sơn** | Kiểm thử và kiểm chứng độc lập |
| **Ly** | Biên tập báo cáo PDF, README và slide thuyết trình |

## Thư mục

| Thư mục | Nội dung |
|---|---|
| [docs/](docs/) | Tài liệu kỹ thuật, sơ đồ và báo cáo PDF |
| [src/](src/) | Mã mô phỏng |
| [tests/](tests/) | Bộ kiểm thử |
| [data/](data/) | Bảng trang, đầu vào, kết quả dự kiến và kết quả chạy |
| [data/traces/](data/traces/) | Trace từng bước dịch địa chỉ |
| [verification/](verification/) | Bằng chứng tính độc lập |
| [presentation/](presentation/) | Slide hoặc video trình bày |

## Chạy và tái tạo kết quả

Dùng Python 3 từ thư mục gốc. Simulator và bộ kiểm tra dùng thư viện chuẩn.

```sh
python3 src/translate.py data/integration_cases.json
python3 tests/integration.py
```

Lệnh đầu in kết quả và trace ra stdout. Lệnh thứ hai đối chiếu với [expected](data/expected_results.json), ghi [kết quả từng ca](data/actual_results.json) và [ba trace mẫu](data/traces/integration.json). Xem [tài liệu kỹ thuật](docs/TECHNICAL_DOC.md) và [cách tính độc lập](verification/byte-ranges.md).
