from homework1.task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum(nums=[1, 3, -1, -3, 5, 3, 6, 7],
                                     k=3) == 16
    assert find_maximal_subarray_sum(nums=[0, 0, 0, 0, 0], k=2) == 0
    assert find_maximal_subarray_sum(nums=[1, 2, 3, 4, 5, 6], k=1) == 6
