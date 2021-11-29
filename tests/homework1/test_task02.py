from homework1.task02 import check_fibonacci


def test_check_fibonacci_return_true_on_fib_sequence_from_0_to_5():
    assert check_fibonacci([0, 1, 1, 2, 3, 5])


def test_check_fibonacci_return_true_on_fib_sequence_from_double_1_to_8():
    assert check_fibonacci([1, 1, 2, 3, 5, 8])


def test_check_fibonacci_return_true_on_fib_sequence_from_single_1_to_8():
    assert check_fibonacci([1, 2, 3, 5, 8])


def test_check_fibonacci_return_false_on_non_fib_positive_sequence():
    assert not check_fibonacci([1, 3, 4, 7, 11])


def test_check_fibonacci_return_false_on_non_fib_negative_sequence():
    assert not check_fibonacci([-1, -1, -2, -3, -5])


def test_check_fibonacci_return_false_on_non_fib_range_sequence():
    assert not check_fibonacci(range(10))


def test_check_fibonacci_return_false_on_empty_data_sequence():
    assert not check_fibonacci([])
