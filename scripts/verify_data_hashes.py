from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from axz_cube_digit_182764125.core import EXPECTED_HASHES, sha256_file


def verify_sha256sums() -> None:
    sums_path = ROOT / "certificates" / "SHA256SUMS.txt"
    for line in sums_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        rel = rel.strip()
        actual = sha256_file(ROOT / rel)
        if actual != digest:
            raise AssertionError(f"SHA256SUMS mismatch for {rel}: expected {digest}, got {actual}")


def main() -> None:
    data_dir = ROOT / "data"
    for filename, expected in EXPECTED_HASHES.items():
        actual = sha256_file(data_dir / filename)
        if actual != expected:
            raise AssertionError(f"hash mismatch for {filename}: expected {expected}, got {actual}")

    cert = json.loads((ROOT / "certificates" / "certificate.json").read_text(encoding="utf-8"))
    hash_map = {
        "all_values_sorted_txt_sha256": EXPECTED_HASHES["all_values_sorted.txt"],
        "positive_values_sorted_txt_sha256": EXPECTED_HASHES["positive_values_sorted.txt"],
        "nonpositive_values_sorted_txt_sha256": EXPECTED_HASHES["nonpositive_values_sorted.txt"],
        "negative_values_sorted_txt_sha256": EXPECTED_HASHES["negative_values_sorted.txt"],
        "all_interval_values_sorted_txt_sha256": EXPECTED_HASHES["all_interval_values_sorted.txt"],
        "witnesses_1_to_4771_tsv_sha256": EXPECTED_HASHES["witnesses_1_to_4771.tsv"],
    }
    for key, expected in hash_map.items():
        actual = cert["hashes"][key]
        if actual != expected:
            raise AssertionError(f"certificate hash mismatch for {key}")

    verify_sha256sums()
    print("PASS: DATA_HASHES_AND_SHA256SUMS_LEDGER")


if __name__ == "__main__":
    main()
