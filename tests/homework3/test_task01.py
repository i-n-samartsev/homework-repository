from functools import partial

from homework3.task01 import cache


def test_cache():
    def func(a, b):
        return (a ** b) ** 2

    cache_func = partial(cache, func, 1)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    val_3 = cache_func(*some)

    assert (val_1 is val_2) and not (val_1 is val_3)
