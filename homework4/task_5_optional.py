"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation
in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
['1', '2', 'Fizz', '4', 'Buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizz(number):
    return 'Fizz' * (not number % 3)


def buzz(number):
    return 'Buzz' * (not number % 5)


def fizzbuzz(n: int) -> Generator:
    """
    Takes a number N as an input and returns a generator that
    yields N FizzBuzz numbers.

    >>> list(fizzbuzz(5))
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> list(fizzbuzz(20))[14]
    'FizzBuzz'
    """

    return (f'{fizz(i)}{buzz(i)}' or str(i) for i in range(1, n + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
