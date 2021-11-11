import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "input_data, output_data",
    [("test_task03_data", (3, 56))]
)
def find_maximum_and_minimum(input_data, output_data):
    min_val, max_val = output_data
    assert find_maximal_subarray_sum(input_data) == output_data
