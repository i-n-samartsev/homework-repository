import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    "input_data, output_data", [([0, 1, 1, 2, 3], True), ([0, 1], True)]
)
def test_positive(input_data, output_data):
    assert check_fibonacci(input_data) == output_data


@pytest.mark.parametrize(
    "input_data, output_data", [([1, 0, 1], False), ([-1, 0, 1], False)]
)
def test_negative(input_data, output_data):
    assert check_fibonacci(input_data) == output_data
