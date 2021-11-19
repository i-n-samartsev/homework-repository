import pytest

from homework3.task04 import is_armstrong


@pytest.mark.parametrize(
    "input_data, output_data", [(9, True), (153, True), (10, False)]
)
def test_is_armstrong(input_data, output_data):
    assert is_armstrong(input_data) == output_data
