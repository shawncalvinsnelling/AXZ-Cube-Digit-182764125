def test_python_int_is_arbitrary_precision():
    x = 2 ** 100
    y = x * x + 123
    assert y > 2 ** 128
    assert y - x * x == 123
