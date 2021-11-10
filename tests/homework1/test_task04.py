import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    "input_data, output_data",
    [(([0, 1], [1, 2], [2, 3], [-2, -4]), 3)]
)
def test_check_sum_of_four(input_data, output_data):
    a, b, c, d = input_data
    assert check_sum_of_four(a, b, c, d) == output_data
