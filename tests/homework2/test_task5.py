import string
import pytest

from homework2.task5 import custom_range


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        ((string.ascii_lowercase, "g"), ["a", "b", "c", "d", "e", "f"]),
        (
            (string.ascii_lowercase, "g", "p"),
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ((string.ascii_lowercase, "p", "g", -2), ["p", "n", "l", "j", "h"]),
    ],
)
def test_positive(input_data, output_data):
    assert custom_range(*input_data) == output_data
