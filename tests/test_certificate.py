from axz_cube_digit_182764125.core import EXPECTED, assert_expected_summary, full_values


def test_expected_summary():
    summary = assert_expected_summary()
    assert summary["first_missing_positive_integer"] == 4772
    assert summary["consecutive_positive_integers_from_1"] == 4771
    assert summary["boundary_witness_expression"] == '(1+((8+2)*(7+((6+41)*(2*5)))))'


def test_frontier_is_complete_and_wall_is_absent():
    values = full_values()
    assert all(n in values for n in range(1, 4771 + 1))
    assert 4772 not in values
