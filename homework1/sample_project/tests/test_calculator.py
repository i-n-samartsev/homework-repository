import pytest


from calculator.calc import check_power_of_2


@pytest.mark.parametrize("num, output", [(65536, True), (-17, False)])
def test_check_power_of_2(num, output):
    assert check_power_of_2(num) == output
