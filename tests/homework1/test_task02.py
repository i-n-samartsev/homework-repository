from homework1.task02 import check_fibonacci


def test_1_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])


def test_2_check_fibonacci():
    assert not check_fibonacci([0, 1, 1, 2, 6])
