"""Translate byte addresses through a single-level page table."""

import argparse
import json
import sys
from pathlib import Path


def is_nonnegative_integer(value):
    return type(value) is int and value >= 0


def valid_entry(entry):
    if not isinstance(entry, dict) or "frame" not in entry:
        return False
    valid = entry.get("valid")
    frame = entry["frame"]
    return type(valid) is int and (
        (valid == 0 and frame is None)
        or (valid == 1 and is_nonnegative_integer(frame))
    )


def load_input(path):
    def reject_constant(value):
        raise ValueError(f"invalid JSON constant {value}")

    config = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_constant)
    if not isinstance(config, dict):
        raise ValueError("expected an input object")
    size = config.get("page_size")
    table = config.get("page_table")
    addresses = config.get("addresses")
    if type(size) is not int or size <= 0:
        raise ValueError("page_size must be a positive integer")
    if not isinstance(table, list) or not all(map(valid_entry, table)):
        raise ValueError("page_table must be an array of valid entries")
    if not isinstance(addresses, list):
        raise ValueError("addresses must be an array")
    return size, table, addresses


def translate(address, size, table):
    trace = []
    result = dict(
        logical_address=address, page=None, offset=None,
        frame=None, physical_address=None, trace=trace,
    )

    def record(step, **details):
        trace.append(dict(step=step, **details))

    def finish(error=None):
        status = "ok" if error is None else "error"
        record("result", status=status, error=error)
        return dict(result, status=status, error=error)

    passed = is_nonnegative_integer(address)
    record("validate_address", logical_address=address, passed=passed)
    if not passed:
        return finish("INVALID_ADDRESS")

    page, offset = divmod(address, size)
    result.update(page=page, offset=offset)
    record("split", page_size=size, page=page, offset=offset)
    passed = page < len(table)
    record("check_page", page=page, page_count=len(table), passed=passed)
    if not passed:
        return finish("PAGE_OUT_OF_RANGE")

    entry = table[page]
    record("check_valid", page=page, valid=entry["valid"])
    if entry["valid"] == 0:
        return finish("INVALID_ENTRY")

    frame = entry["frame"]
    record("read_frame", frame=frame)
    physical_address = frame * size + offset
    record("compute_pa", frame=frame, page_size=size, offset=offset,
           physical_address=physical_address)
    result.update(frame=frame, physical_address=physical_address)
    return finish()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        size, table, addresses = load_input(args.input)
        output = [translate(address, size, table) for address in addresses]
        print(json.dumps(output, indent=2, allow_nan=False))
    except (OSError, ValueError) as error:
        print(f"INVALID_INPUT: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
