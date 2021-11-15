import pytest

from homework2.task2 import major_and_minor_elem


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        ([3, 2, 3], (3, 2)),
        ([2,2,1,1,1,2,2], (2, 1))
    ],
)
def test_positive(input_data, output_data):
    assert major_and_minor_elem(input_data) == *output_data
