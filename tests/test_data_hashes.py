from pathlib import Path
from axz_cube_digit_182764125.core import EXPECTED_HASHES, sha256_file

ROOT = Path(__file__).resolve().parents[1]


def test_data_hashes():
    for filename, expected in EXPECTED_HASHES.items():
        assert sha256_file(ROOT / "data" / filename) == expected
