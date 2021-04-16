from homework1.task05 import find_maximal_subarray_sum


def test1():
    """Testing example from task"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test2():
    """Testing when subarray length = 0"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 0) == 0


def test3():
    """Testing with empty array"""
    assert find_maximal_subarray_sum([], 3) == float('-inf')
