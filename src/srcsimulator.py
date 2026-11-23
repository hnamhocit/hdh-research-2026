import argparse
import json
import os
from pathlib import Path


def translate_address(logical_address: int, page_size: int, page_table: list[dict]) -> dict:
    trace = [f"Input: LA = {logical_address}, Page Size (P) = {page_size}"]

    if not isinstance(logical_address, int) or isinstance(logical_address, bool) or logical_address < 0:
        trace.append("Validation Failed: Logical address must be a non-negative integer.")
        return {
            "status": "ERROR",
            "result": "INVALID_ADDRESS",
            "page": None,
            "offset": None,
            "frame": None,
            "physical_address": None,
            "trace": trace,
        }

    page_number = logical_address // page_size
    offset = logical_address % page_size
    trace.append(f"Address Split: page = floor({logical_address} / {page_size}) = {page_number}, offset = {logical_address} mod {page_size} = {offset}")

    if page_number >= len(page_table):
        trace.append(f"Bounds Check Failed: page {page_number} is out of range [0..{len(page_table) - 1}].")
        return {
            "status": "ERROR",
            "result": "PAGE_OUT_OF_RANGE",
            "page": page_number,
            "offset": offset,
            "frame": None,
            "physical_address": None,
            "trace": trace,
        }

    entry = page_table[page_number]
    if not entry.get("valid", False):
        trace.append(f"Valid-Bit Check Failed: page {page_number} is marked INVALID (valid = 0).")
        return {
            "status": "ERROR",
            "result": "INVALID_ENTRY",
            "page": page_number,
            "offset": offset,
            "frame": None,
            "physical_address": None,
            "trace": trace,
        }

    frame_number = entry["frame"]
    physical_address = frame_number * page_size + offset
    trace.append(f"Page Table Lookup: page {page_number} -> valid = 1, frame = {frame_number}")
    trace.append(f"Physical Address: PA = {frame_number} * {page_size} + {offset} = {physical_address}")

    return {
        "status": "SUCCESS",
        "result": f"PA {physical_address}",
        "page": page_number,
        "offset": offset,
        "frame": frame_number,
        "physical_address": physical_address,
        "trace": trace,
    }


def run_batch(input_path: str, output_path: str, trace_dir: str) -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    page_size = config["page_size"]
    if page_size <= 0 or (page_size & (page_size - 1)) != 0:
        raise ValueError("Page size must be a positive power of 2.")

    page_table = config["page_table"]
    test_cases = config["test_cases"]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    os.makedirs(trace_dir, exist_ok=True)

    results = []
    for tc in test_cases:
        tc_id = tc["id"]
        la = tc["logical_address"]
        expected = tc.get("expected")

        output = translate_address(la, page_size, page_table)
        actual = output["result"]
        passed = (actual == expected) if expected is not None else None

        record = {
            "id": tc_id,
            "description": tc.get("description", ""),
            "logical_address": la,
            "expected": expected,
            "actual": actual,
            "pass_fail": "PASS" if passed else "FAIL",
            "details": {
                "page": output["page"],
                "offset": output["offset"],
                "frame": output["frame"],
                "physical_address": output["physical_address"],
            },
        }
        results.append(record)

        trace_file = Path(trace_dir) / f"{tc_id}_trace.txt"
        with open(trace_file, "w", encoding="utf-8") as tf:
            tf.write(f"=== TRACE FOR {tc_id}: {tc.get('description', '')} ===\n")
            tf.write("\n".join(output["trace"]) + "\n")
            tf.write(f"Final Result: {actual}\n")

    with open(output_path, "w", encoding="utf-8") as out_f:
        json.dump({"page_size": page_size, "results": results}, out_f, indent=2, ensure_ascii=False)

    print(f"Executed {len(results)} test cases. Results saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Single-Level Page Table Address Translation Simulator")
    parser.add_argument("--input", default="data/integration_cases.json", help="Path to input JSON file")
    parser.add_argument("--output", default="data/actual_results.json", help="Path to output JSON file")
    parser.add_argument("--traces", default="data/traces", help="Directory to save step-by-step traces")
    args = parser.parse_args()

    run_batch(args.input, args.output, args.traces)
