# In previous homework task 4, you wrote a cache function that remembers other
# function output value. Modify it to be a parametrized decorator.

from typing import Any, Callable
from dataclasses import dataclass


@dataclass
class ValueNumber:
    """
    Keeps the function result and the number of times that it can be
    taken from cache.
    """
    value: Any
    number: int


def cache(times: int) -> Callable:
    """
    Parametrized decorator, that remembers function output value only 'times'
    """

    baggage_room = {}

    def decorator(func: Callable) -> Callable:

        def wrapper(*args, **kwargs):
            kwargs = {key: kwargs[key] for key in sorted(kwargs)}
            key = str(args) + str(kwargs)

            if key not in baggage_room or baggage_room[key].number == 0:
                baggage_room[key] = ValueNumber(value=func(*args, **kwargs),
                                                number=times + 1)

            baggage_room[key].number -= 1
            return baggage_room[key].value
        return wrapper
    return decorator
