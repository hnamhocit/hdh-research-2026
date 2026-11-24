"""
Tính expected result ĐỘC LẬP cho ma trận test của nhóm (RESEARCH_PLAN.md, mục 7).

Script này KHÔNG import và KHÔNG sao chép logic của chương trình chính. Cách tính khác hẳn:
không dùng phép chia nguyên và chia lấy dư. Script đếm số khối P byte đầy đủ nằm trong LA
để ra số trang, rồi offset = LA - đầu khối. Sau đó mới tra bảng.

Page table (theo docs/specification.md: 4 entry, trang 1 có valid = 0; frame của trang 0, 2, 3
suy ra từ expected của nhóm): page 0 -> frame 3, page 1 -> invalid, page 2 -> frame 7, page 3 -> frame 0.

Chạy:  python expected_independent.py   (ghi expected_results.csv)
"""
import csv
import os

P = 16
PAGE_TABLE = [      # chỉ số = số page; (frame, valid)
    (3, 1),
    (None, 0),
    (7, 1),
    (0, 1),
]

# (mã test, LA, expected nhóm ghi trong RESEARCH_PLAN.md, mô tả)
CASES = [
    ("T01", 37, "117", "Hợp lệ, page 2"),
    ("T02", 51, "3", "Hợp lệ, page 3"),
    ("T03", 5, "53", "Hợp lệ, page 0"),
    ("T04", 48, "0", "Offset = 0"),
    ("T05", 63, "15", "Offset = P - 1"),
    ("T06", 64, "PAGE_OUT_OF_RANGE", "Page ngoài bảng"),
    ("T07", 16, "INVALID_ENTRY", "Entry invalid"),
    ("T08", -1, "INVALID_ADDRESS", "Địa chỉ âm"),
]


def independent_expected(la, page_size=P, page_table=PAGE_TABLE):
    """Trả dict cùng trường với đầu ra của đặc tả (status, page, offset, frame, physical_address, error)."""
    res = {"status": "error", "page": None, "offset": None, "frame": None,
           "physical_address": None, "error": None}
    if isinstance(la, bool) or not isinstance(la, int) or la < 0:
        res["error"] = "INVALID_ADDRESS"
        return res
    page, start = 0, 0                      # đếm số khối đầy đủ, không dùng // và %
    while start + page_size <= la:
        start += page_size
        page += 1
    res["page"], res["offset"] = page, la - start
    if page >= len(page_table):
        res["error"] = "PAGE_OUT_OF_RANGE"
        return res
    frame, valid = page_table[page]
    if valid != 1:
        res["error"] = "INVALID_ENTRY"
        return res
    res.update(status="ok", frame=frame, physical_address=frame * page_size + res["offset"])
    return res


def summary(res):
    return str(res["physical_address"]) if res["status"] == "ok" else res["error"]


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expected_results.csv")
    bad = 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "page_size", "logical_address", "page", "offset", "frame",
                    "expected_independent", "expected_nhom", "khop", "mo_ta"])
        for cid, la, group_exp, note in CASES:
            r = independent_expected(la)
            ok = summary(r) == group_exp
            bad += (not ok)
            w.writerow([cid, P, la, r["page"], r["offset"], r["frame"], summary(r), group_exp,
                        "KHOP" if ok else "LECH", note])
            print(f"{cid}: LA={la:>3} page={r['page']} offset={r['offset']} frame={r['frame']} -> "
                  f"{summary(r):<18} nhóm ghi: {group_exp:<18} {'KHỚP' if ok else 'LỆCH'}")
    print(f"\n{len(CASES) - bad}/{len(CASES)} khớp với expected của nhóm.")
