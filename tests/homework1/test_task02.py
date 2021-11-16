from homework1.task02 import check_fibonacci


def test_check_fibonacci_return_true_on_fibonacci_sequence():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])


def test_check_fibonacci_return_false_on_non_fibonacci_sequence():
    assert not check_fibonacci([0, 1, 1, 2, 6])
