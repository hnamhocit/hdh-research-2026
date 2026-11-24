"""
Đối chiếu file kết quả của nhóm (data/actual_results.json) với expected tính ĐỘC LẬP.

Với mỗi test, script kiểm tra:
  1. `expected` nhóm ghi có khớp expected độc lập không.
  2. `actual` có khớp expected độc lập không (status, page, offset, frame, physical_address, error).
  3. Chuỗi bước trong `trace` có đúng thứ tự theo docs/TECHNICAL_DOC.md không, và giá trị trong trace
     có nhất quán với kết quả không.
  4. Trường `result` (PASS/FAIL) nhóm ghi có đúng với việc so sánh thật không.

Lưu ý: script chỉ kiểm tra DỮ LIỆU đã ghi trong file. Nó không chạy chương trình dịch địa chỉ. Muốn có
actual mới, chạy `python3 src/translate.py <input.json>` rồi đưa kết quả vào cùng định dạng.

Hỗ trợ hai định dạng đầu vào:
  - Mảng kết quả thô do `python src/translate.py ...` in ra (không có expected). Script tự tính expected
    độc lập từ `logical_address`, so với kết quả thật và GHI file ket_qua_doi_chieu.csv.
  - File data/actual_results.json của nhóm (mỗi test có `expected`, `actual`, `result`).

Chạy:  python verify_actual.py ket_qua_cua_son.json
       python verify_actual.py data/actual_results.json
"""
import csv
import json
import os
import sys

from expected_independent import CASES, independent_expected, summary

FIELDS = ("status", "page", "offset", "frame", "physical_address", "error")
TRACE_OK = ["validate_address", "split", "check_page", "check_valid", "read_frame", "compute_pa", "result"]
TRACE_BY_ERROR = {
    "PAGE_OUT_OF_RANGE": ["validate_address", "split", "check_page", "result"],
    "INVALID_ENTRY": ["validate_address", "split", "check_page", "check_valid", "result"],
    "INVALID_ADDRESS": ["validate_address", "result"],
}


def diff(a, b):
    return [f"{k}: {a.get(k)!r} != {b.get(k)!r}" for k in FIELDS if a.get(k) != b.get(k)]


def check_trace(actual, ind):
    problems = []
    steps = [s["step"] for s in actual["trace"]]
    want = TRACE_OK if ind["status"] == "ok" else TRACE_BY_ERROR[ind["error"]]
    if steps != want:
        problems.append(f"trace sai thứ tự: {steps} (cần {want})")
    for s in actual["trace"]:
        if s["step"] == "split" and (s["page"], s["offset"]) != (ind["page"], ind["offset"]):
            problems.append("trace split không khớp")
        if s["step"] == "compute_pa" and s["physical_address"] != ind["physical_address"]:
            problems.append("trace compute_pa không khớp")
    return problems


def main(path):
    with open(path, encoding="utf-8-sig") as f:
        tests = json.load(f)
    ids = {la: cid for cid, la, _, _ in CASES}
    all_ok = True
    rows = []
    for idx, t in enumerate(tests):
        if "actual" in t:                                   # định dạng actual_results.json của nhóm
            actual, stored_expected, stored_result = t["actual"], t["expected"], t.get("result")
            cid = t["id"]
        else:                                               # mảng kết quả thô của translate.py
            actual, stored_expected, stored_result = t, None, None
            cid = ids.get(t["logical_address"], f"#{idx + 1}")
        la = actual["logical_address"]
        ind = independent_expected(la)
        problems = [f"actual lệch độc lập: {d}" for d in diff(actual, ind)]
        if stored_expected is not None:
            problems += [f"expected nhóm lệch độc lập: {d}" for d in diff(stored_expected, ind)]
        problems += check_trace(actual, ind)
        mine = "PASS" if not problems else "FAIL"
        if stored_result is not None and mine != stored_result:
            problems.append(f"trường result nhóm ghi là {stored_result} nhưng đối chiếu ra {mine}")
        all_ok &= (not problems)
        print(f"{cid} LA={la:>3}: {mine}" + ("" if not problems else "  <- " + "; ".join(problems)))
        rows.append([cid, la, summary(ind), summary(actual), mine])
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ket_qua_doi_chieu.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "logical_address", "expected_independent", "actual_result", "pass_fail"])
        w.writerows(rows)
    print("\nTất cả khớp." if all_ok else "\nCó chỗ lệch, xem chi tiết ở trên.")
    print("Đã ghi", out)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data/actual_results.json"))
