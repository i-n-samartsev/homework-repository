from homework1.task05 import find_maximal_subarray_sum


def test_1_find_maximal_subarray_sum_on_a_varied_data():
    assert find_maximal_subarray_sum(nums=[1, 3, -3, -5, 3, 6, 7], k=3) == 16


def test_find_maximal_subarray_sum_on_a_monotonous_data():
    assert find_maximal_subarray_sum(nums=[0, 0, 0, 0, 0], k=2) == 0


def test_3_find_maximal_subarray_sum_on_a_serial_data():
    assert find_maximal_subarray_sum(nums=[1, 2, 3, 4, 5, 6], k=1) == 6
