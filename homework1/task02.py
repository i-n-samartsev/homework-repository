"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
     and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence, Generator, Iterable


def fibonacci_generator(starting_item: int = 0,
                        double_one: bool = True) -> Generator:
    """
    Generates an endless fibonacci sequence from 'starting_item'.

    As number one occurs twice in the fibonacci sequence, parameter
    'double_one' is responsible for the number of generated
    units in the sequence.

    If 'starting_item' == 1 and 'double_one' is True -> 1, 1, 2, 3, 5, 8, ...
    If 'starting_item' == 1 and 'double_one' is False -> 1, 2, 3, 5, 8, ...
    """
    current_elem, next_elem = 0, 1

    while True:
        if current_elem == 1 and not double_one:
            double_one = True
        elif current_elem >= starting_item:
            yield current_elem
        current_elem, next_elem = next_elem, current_elem + next_elem


empty_element = object()  # sentinel object


def peek_first_two_elem_twice(iterable: Iterable) -> Generator:
    """
    Return a tuple of first two elements of 'iterable', than elements
    from beginning.
    """
    iterable = iter(iterable)
    first_elem = next(iterable, empty_element)
    second_elem = next(iterable, empty_element)
    yield first_elem, second_elem
    yield first_elem
    yield second_elem
    for element in iterable:
        yield element


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Checks if 'data' is a Fibonacci Sequence.
    """
    data = peek_first_two_elem_twice(data)
    starting_two_items = next(data)
    if starting_two_items[0] is empty_element:
        return False  # empty data sequence
    double_one = False if starting_two_items == (1, 2) else True
    fib_gen = fibonacci_generator(starting_two_items[0], double_one)
    for our_elem, true_elem in zip(data, fib_gen):
        if our_elem != true_elem:
            return False
    return True
