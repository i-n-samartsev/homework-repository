from homework3.task02 import time_work_fun_value, slow_calculate


def test_timework_slow_calculate():
    assert time_work_fun_value(slow_calculate, [i for i in range(1, 501)]) < 60
