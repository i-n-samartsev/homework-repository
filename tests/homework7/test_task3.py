import pytest

from homework7.task3 import tic_tac_toe_checker


@pytest.mark.parametrize(
    "input_data, output_data",
    [
        ([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]], "unfinished"),
        ([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]], "x wins!"),
        (
            [["-", "-", "o", "o"], ["-", "o", "o", "o"], ["x", "x", "x", "x"]],
            "x wins!",
        ),
    ],
)
def test_tic_tac_toe_checker(input_data, output_data):
    assert tic_tac_toe_checker(input_data) == output_data
