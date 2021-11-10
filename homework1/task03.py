"""
Write down the function, which reads input line-by-line, and find maximum
and minimum values. Function should return a tuple with
the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    max_value = float('-inf')
    min_value = float('inf')
    with open(file=file_name, mode='r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            max_value = max(max_value, *numbers)
            min_value = min(min_value, *numbers)
    return min_value, max_value
