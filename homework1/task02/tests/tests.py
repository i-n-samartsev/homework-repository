from main.task02 import check_fibonacci


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_fibonacci([0, 1, 1, 2, 3])


def test_negative_case():
    """Testing that non-powers of 2 give False"""
    assert not check_fibonacci([1, 0, 2])
