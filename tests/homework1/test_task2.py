import pytest


from homework1.task2 import check_fibonacci


@pytest.mark.parametrize(
        'test_input, expected',
        [[[0, 1, 1, 2, 3], True], [[0, 1], True]]
)
def test_positive_case(test_input, expected):
    """Testing that actual powers of 2 give True"""
    assert check_fibonacci(test_input) == expected


@pytest.mark.parametrize(
        'test_input, expected',
        [[[0, 1, 1, 2, 6], False], [[0], False]]
)
def test_negative_case(test_input, expected):
    """Testing that non-powers of 2 give False"""
    assert check_fibonacci(test_input) == expected
