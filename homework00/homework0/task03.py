"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def read_file(file_name: str) -> list:
    minimum, maximum = 0, 0
    with open(file_name) as f:
        for line in f:
            if len(line.strip()) > 0:
                value = int(line.strip())
                if value > maximum:
                    maximum = value
                elif value < minimum:
                    minimum = value

    return minimum, maximum


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    minimum, maximum = read_file(file_name)
    return (minimum, maximum)
