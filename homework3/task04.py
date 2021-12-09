"""
Armstrong number is a number that is the sum of its own digits each raised to
the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number
in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:

    """ Detects if a number is Armstrong number """

    if number < 0:
        raise ValueError('Parameter "number" must be > 0')

    digits = [int(i) for i in list(str(number))]
    powered_digits = map(lambda i, length=len(digits): i ** length, digits)
    return sum(powered_digits) == number
