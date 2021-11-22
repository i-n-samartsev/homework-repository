"""
Write a function that takes a number N as an input and returns
N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран,
чисть картошку!"
"""
from typing import List


def fizz(number):
    return 'Fizz' * (not number % 3)


def buzz(number):
    return 'Buzz' * (not number % 5)


def fizzbuzz(n: int) -> List[str]:
    """
    Takes a number N as an input and returns N FizzBuzz numbers.

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(20)[14]
    'FizzBuzz'
    """

    return [f'{fizz(i)}{buzz(i)}' or str(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
