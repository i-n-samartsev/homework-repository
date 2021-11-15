# In previous homework task 4, you wrote a cache function that remembers other
# function output value. Modify it to be a parametrized decorator,
# so that the following code:

from typing import Callable


def cache(times: int) -> Callable:
    baggage_room = {}

    def decorator(func: Callable) -> Callable:

        def wrapper(*some):
            if some not in baggage_room:
                baggage_room[some] = [func(*some), times]

            if baggage_room[some][1]:
                baggage_room[some][1] -= 1
                return baggage_room[some]

        return wrapper

    return decorator


@cache(times=3)
def some_function():
    pass

# Would give out cached value up to times number only. Example:


@cache(times=2)
def f():
    return input('? ')

# >>> f()
# ? 1
# '1'
# >>> f()     # will remember previous value
# '1'
# >>> f()     # but use it up to two times only
# '1'
# >>> f()
# ? 2
# '2'
