"""
In previous homework task 4, you wrote a cache function that remembers other
function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')
        # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from functools import lru_cache
from typing import Callable

TIMES_CALL_FUNC = {}


@lru_cache()
def compute(func: Callable, *args):
    return func(*args)


def cache(func: Callable, times: int, *args):
    global TIMES_CALL_FUNC
    if args not in TIMES_CALL_FUNC:
        TIMES_CALL_FUNC.update([(args, 0)])
    elif TIMES_CALL_FUNC[args] < times:
        TIMES_CALL_FUNC[args] += 1
    else:
        TIMES_CALL_FUNC[args] = 0
        compute.cache_clear()

    return compute(func, *args)
