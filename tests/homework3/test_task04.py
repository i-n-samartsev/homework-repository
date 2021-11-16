from homework3.task04 import is_armstrong


def test_is_armstrong_true():
    assert is_armstrong(153) is True


def test_2_is_armstrong_false():
    assert is_armstrong(10) is False
