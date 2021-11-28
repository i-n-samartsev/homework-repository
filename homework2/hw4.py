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
from collections import OrderedDict
from typing import Callable


def cache(function: Callable) -> Callable:
    """
    Decorator that caches a function calls.
    """
    baggage_room = {}

    def wrapper(*args, **kwargs):
        kwargs = OrderedDict(sorted(kwargs.items(), key=lambda t: t[0]))
        key = str(args) + str(kwargs)
        if key not in baggage_room:
            baggage_room[key] = function(*args, **kwargs)
        return baggage_room[key]

    return wrapper
