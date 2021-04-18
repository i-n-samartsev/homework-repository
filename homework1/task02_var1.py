"""Task02_var1 - Fibonacci"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:

    """Checking if the sequence is 'The Fibonacci Sequence' """

    if len(data) > 2 and data[0] == 0 and data[1] == 1:
        for elem in range(len(data) - 1):
            if data[elem + 1] == data[elem] + data[elem - 1]:
                continue
        if data[-1] == data[-2] + data[-3]:
            return True
    return False
