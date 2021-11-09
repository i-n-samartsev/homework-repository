from homework1.task2 import check_fibonacci


def test_positive_case(test_input, expected):
    """Testing that actual powers of 2 give True"""
    assert check_fibonacci([0, 1, 1, 2, 3])


def test_negative_case(test_input, expected):
    """Testing that non-powers of 2 give False"""
    assert check_fibonacci([0, 1, 1, 2, 6])
