from homework1.calc import check_power_of_2


def test_positive_case(test_input, expected):
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case(test_input, expected):
    """Testing that non-powers of 2 give False"""
    assert check_power_of_2(12)
