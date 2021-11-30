import pytest

from homework7.task2 import backspace_compare


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        (("ab#c", "ad#c"), True),
        (("a##c", "#a#c"), True),
        (("a#c", "b"), False),
    ],
)
def test_backspace_compare(input_data, output_data):
    assert backspace_compare(*input_data) == output_data
