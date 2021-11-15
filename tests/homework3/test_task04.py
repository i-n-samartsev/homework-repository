from homework3.task04 import is_armstrong


def test_1_is_armstrong():
    assert is_armstrong(153) is True


def test_2_is_armstrong():
    assert is_armstrong(10) is False
