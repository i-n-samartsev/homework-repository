import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Any, Callable, Sequence


# Here's a not very efficient calculation function
# that calculates something important:


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


# Calculate total sum of slow_calculate() of all numbers starting from 0 to
# 500. Calculation time should not take more than a minute. Use functional
# capabilities of multiprocessing module. You are not allowed to modify
# slow_calculate function.

def calculating_of_total_sum(function: Callable, args: Sequence[Any]) -> int:
    """
    Asynchronously calculates the sum of the results of a function
    from the arguments
    """

    with Pool(processes=50) as pool:
        results = pool.map(function, args)
    return sum(results)


if __name__ == '__main__':
    result = calculating_of_total_sum(slow_calculate, range(500))
    print(result)
