from homework3.task02 import count_time


def test_timework_slow_calculate():
    assert count_time([i for i in range(1, 501)]) < 60
