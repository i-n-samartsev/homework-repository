"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') \
== ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') \
== ['g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) \
== ['p', 'n', 'l', 'j', 'h']

"""

from typing import Any, AnyStr, Iterable, List


def custom_range(
    iterable: Iterable[AnyStr],
    _arg1: Any = None,
    _arg2: Any = None,
    _arg3: Any = None,
    *,
    start: Any = None,
    stop: Any = None,
    step: Any = None
) -> List:
    """This function implement range function for iterable. Iterable must
    yield chars/strings"""
    # Check that arguments is correct
    kwargs_not_none = start is None or stop is None or step is None
    pos_args_not_none = _arg1 is None or _arg2 is None or _arg3 is None

    if _arg1 is not None and _arg2 is None and _arg3 is None and kwargs_not_none:
        stop = _arg1
        step = 1
    elif _arg1 is not None and _arg2 is not None and _arg3 is None and kwargs_not_none:
        start = _arg1
        stop = _arg2
        step = 1
    elif (
        _arg1 is not None
        and _arg2 is not None
        and _arg3 is not None
        and kwargs_not_none
    ):
        start = _arg1
        stop = _arg2
        step = _arg3
    elif pos_args_not_none:
        if start is None and stop is not None and step is None:
            step = 1
        elif start is not None and stop is not None and step is None:
            step = 1
        elif start is not None and stop is not None and step is not None:
            pass  # is ok
        else:
            raise ValueError("Bad function's arguments")
    else:
        raise ValueError("Bad function's arguments")

    iterable = list(iterable)
    # Find start position
    if start is not None:
        start = iterable.index(start)
    else:
        start = 0
    # Find stop position
    stop = iterable.index(stop)

    output_list = []
    for i in range(start, stop, step):
        output_list.append(iterable[i])
    return output_list
