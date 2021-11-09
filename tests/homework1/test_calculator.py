import pytest


from homework1.calc import check_power_of_2


@pytest.mark.parametrize(
        'test_input, expected',
        [[65536, True], [16, True], [2, True]]
)
def test_positive_case(test_input, expected):
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(test_input) == expected


@pytest.mark.parametrize(
        'test_input, expected',
        [[12, False], [5, False], [-1, False]]
)
def test_negative_case(test_input, expected):
    """Testing that non-powers of 2 give False"""
    assert check_power_of_2(test_input) == expected
