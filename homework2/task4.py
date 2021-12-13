"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    saved_data = {}

    def helper(*args):
        if args in saved_data.keys():
            return saved_data[args]
        else:
            val_func = func(*args)
            saved_data.update([(args, val_func)])
            return val_func

    return helper
