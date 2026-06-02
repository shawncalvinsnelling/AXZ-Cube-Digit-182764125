from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from axz_cube_digit_182764125.core import EXPECTED, EXPECTED_HASHES, assert_expected_summary


def main() -> None:
    checked = json.loads((ROOT / "certificates" / "certificate.json").read_text(encoding="utf-8"))
    summary = assert_expected_summary()

    for key in (
        "possible_cut_patterns",
        "unique_integer_values_generated",
        "positive_integer_values_generated",
        "non_positive_integer_values_generated",
        "negative_integer_values_generated",
        "zero_present",
        "consecutive_positive_integers_from_1",
        "first_missing_positive_integer",
        "minimum_integer_value",
        "maximum_integer_value",
        "all_interval_unique_values_generated",
    ):
        if checked["certificate"][key] != summary[key]:
            raise AssertionError(f"certificate mismatch for {key}")

    if checked["certificate"]["boundary_witness"]["expression"] != summary["boundary_witness_expression"]:
        raise AssertionError("boundary witness mismatch")

    print("PASS: GENERATED_CERTIFICATE_MATCHES_CHECKED_CERTIFICATE")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
