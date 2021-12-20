from homework3.task01 import wrapper_cache


def test_cache():
    @wrapper_cache(times=1)
    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200

    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)

    assert (val_1 is val_2) and not (val_1 is val_3)
