from homework3.task02 import stopswatch


def test_is_armstrong():
    assert stopswatch([i for i in range(1, 501)]) < 60
