from axz_cube_digit_182764125.core import EXPECTED, all_interval_values, interval_values


def test_all_interval_universe_count_and_leafs():
    assert len(all_interval_values()) == EXPECTED["all_interval_unique_values_generated"]
    assert 182764125 in interval_values(0, 9)
    assert 82764125 in interval_values(1, 9)
