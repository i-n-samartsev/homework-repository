import pytest

from homework1.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "input_data, output_data",
    [("homework1\est_task03_data.txt", (3, 56))]
)
def test_find_maximum_and_minimum(input_data, output_data):
    min_val, max_val = output_data
    assert find_maximum_and_minimum(input_data) == min_val, max_val
