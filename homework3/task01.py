# In previous homework task 4, you wrote a cache function that remembers other
# function output value. Modify it to be a parametrized decorator.

from dataclasses import dataclass
from inspect import signature
from typing import Any, Callable


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
        defaults = {}
        sig = signature(func)
        for param in sig.parameters.values():
            if param.default is not param.empty:
                defaults[param.name] = param.default

        def wrapper(*args, **kwargs):
            kwargs = defaults | kwargs
            kwargs = {key: kwargs[key] for key in sorted(kwargs)}
            key = str(args) + str(kwargs)

            if key not in baggage_room or baggage_room[key].number == 0:
                baggage_room[key] = ValueNumber(value=func(*args, **kwargs),
                                                number=times + 1)

            baggage_room[key].number -= 1
            return baggage_room[key].value
        return wrapper
    return decorator
