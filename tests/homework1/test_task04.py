import pytest

from homework1.task04 import check_sum_of_four


@pytest.mark.parametrize(
    "input_d1, input_d2, input_d3, input_d4, output_d",
    [([0, 1], [1, 2], [2, 3], [-2, -4], 3)]
)
def test_check_sum_of_four(input_data, output_data):
    assert check_sum_of_four(input_d1, input_d2,
                             input_d3, input_d4) == output_d
