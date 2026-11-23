# Paging and Page-Table Address Translation

Đồ án Hệ điều hành về dịch địa chỉ logic sang địa chỉ vật lý bằng bảng trang một cấp.

- [Yêu cầu đồ án](REQUIREMENTS.md)
- [Tiến độ và phân công](RESEARCH_PLAN.md)
- [Rà soát tích hợp và hồ sơ tuần 4](docs/integration-review.md#kết-quả-rà-soát-tuần-4)

## Thư mục

| Thư mục | Nội dung |
|---|---|
| [docs/](docs/) | Đặc tả, tài liệu tham khảo và báo cáo PDF |
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

Lệnh đầu in kết quả và trace ra stdout. Lệnh thứ hai đối chiếu với [expected](data/expected_results.json), ghi [kết quả từng ca](data/actual_results.json) và [ba trace mẫu](data/traces/integration.json). Xem [đặc tả](docs/specification.md), [pseudocode](docs/pseudocode.md) và [cách tính độc lập](verification/byte-ranges.md).
