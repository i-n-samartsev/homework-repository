import pytest

from homework1.task02 import check_fibonacci


@pytest.mark.parametrize(
    "input_data, output_data",
    [([0, 1, 1, 2, 3], True),
     ([0, 1], True),
     ([1, 0, 1], False),
     ([0], False),
     ([-1, 0, 1], False)]
)
def test_check_fibonacci(input_data, output_data):
    assert check_fibonacci(input_data) == output_data
