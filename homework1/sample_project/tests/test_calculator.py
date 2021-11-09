import pytest

from calculator.calc import check_power_of_2


@pytest.mark.parametrize("num, output",
                         [(1, True), (65536, True), (3, False), (-17, False)])
def test_check_power_of_2(num, output):
    assert check_power_of_2(num) == output
