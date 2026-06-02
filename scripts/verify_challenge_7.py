from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from axz_cube_digit_182764125.core import DIGIT_STRING, EXPECTED, TRUTH_LABEL, assert_expected_summary, full_values


def main() -> None:
    summary = assert_expected_summary()
    values = full_values()
    missing = EXPECTED["first_missing_positive_integer"]
    frontier = EXPECTED["consecutive_positive_integers_from_1"]
    for n in range(1, frontier + 1):
        if n not in values:
            raise AssertionError(f"missing represented integer inside frontier: {n}")
    if missing in values:
        raise AssertionError(f"first missing integer unexpectedly represented: {missing}")

    print("PASS:", TRUTH_LABEL)
    print(f"DIGIT_STRING={DIGIT_STRING}")
    print(f"CONSECUTIVE_POSITIVES=1..{frontier}")
    print(f"FIRST_MISSING={missing}")
    print(f"UNIQUE_VALUES={summary['unique_integer_values_generated']}")


if __name__ == "__main__":
    main()
