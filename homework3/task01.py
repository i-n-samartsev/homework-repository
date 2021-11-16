# In previous homework task 4, you wrote a cache function that remembers other
# function output value. Modify it to be a parametrized decorator.

from typing import Callable


def cache(times: int) -> Callable:
    """
    Parametrized decorator, that remembers function output value only 'times'
    """

    baggage_room = {}

    def decorator(func: Callable) -> Callable:

        def wrapper(*some):
            if some not in baggage_room or not baggage_room[some][1]:
                baggage_room[some] = [func(*some), times + 1]

            baggage_room[some][1] -= 1
            return baggage_room[some][0]

        return wrapper

    return decorator
