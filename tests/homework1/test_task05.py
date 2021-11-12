import pytest

from homework1.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "input_data, output_data",
    [(([0, 1, -10, 2, 5], 3), 7), (([4, 12, -10, 22, -5], 3), 24)],
)
def test_find_maximal_subarray_sum(input_data, output_data):
    nums, k = input_data
    assert find_maximal_subarray_sum(nums, k) == output_data
