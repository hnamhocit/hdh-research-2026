"""Run the public CLI against the independently calculated expectations."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

SUCCESS_STEPS = [
    "validate_address", "split", "check_page", "check_valid",
    "read_frame", "compute_pa", "result",
]
TRACE_STEPS = {
    None: SUCCESS_STEPS,
    "INVALID_ADDRESS": ["validate_address", "result"],
    "PAGE_OUT_OF_RANGE": SUCCESS_STEPS[:3] + ["result"],
    "INVALID_ENTRY": SUCCESS_STEPS[:4] + ["result"],
}


def main():
    completed = subprocess.run(
        [sys.executable, str(ROOT / "src/translate.py"), str(DATA / "integration_cases.json")],
        check=True, capture_output=True, text=True,
    )
    actual = json.loads(completed.stdout)
    expected = json.loads((DATA / "expected_results.json").read_text())
    if len(actual) != len(expected):
        raise SystemExit(f"Expected {len(expected)} results, received {len(actual)}")

    results = []
    for index, (want, observed) in enumerate(zip(expected, actual), 1):
        summary = {key: value for key, value in observed.items() if key != "trace"}
        trace = observed["trace"]
        passed = (
            summary == want
            and [step["step"] for step in trace] == TRACE_STEPS[want["error"]]
            and trace[-1] == {"step": "result", "status": want["status"], "error": want["error"]}
        )
        outcome = "PASS" if passed else "FAIL"
        results.append(dict(id=f"T{index:02d}", expected=want, actual=observed, result=outcome))
        print(f"T{index:02d} LA={want['logical_address']}: {outcome}")

    (DATA / "actual_results.json").write_text(
        json.dumps(results, indent=2) + "\n", encoding="utf-8",
    )
    samples = {str(row["actual"]["logical_address"]): row["actual"]["trace"]
               for row in results if row["actual"]["logical_address"] in (37, 16, 64)}
    (DATA / "traces/integration.json").write_text(
        json.dumps(samples, indent=2) + "\n", encoding="utf-8",
    )
    return 0 if all(row["result"] == "PASS" for row in results) else 1


if __name__ == "__main__":
    sys.exit(main())
