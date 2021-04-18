"""Task02_var2 - Fibonacci"""

from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Checking if a Sequence of integers is the Fibonacci sequence"""
    length = len(data) - 1
    if length + 1 > 2 and (data[1] == 0 or data[0] == 0 and data[1] == 1):
        for elem in range(length, 1, -1):
            if data[elem] == data[elem - 1] + data[elem - 2]:
                continue
            return False
        return True
    if length + 1 > 2 and (data[1] != 0 or (data[1] != 1 and data[0] != 0)):
        for elem in range(length, 1, -1):
            if data[elem] == data[elem - 1] + data[elem - 2]:
                continue
            return False
        old = data[1]
        old_old = 0
        cur = data[0]
        while cur > 0:
            old_old, old = old, cur
            cur = old_old - cur
        if cur == 0 and old == 1:
            return True
    return False
