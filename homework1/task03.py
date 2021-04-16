"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("test1.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """"
    Reads input line-by-line, and find maximum and minimum values.
    Function should return Tuple (minimum, maximum)

    Input:
    file_name (str)

    Requirements for file:
    each line consist only one (int)value

    Output:
    Tuple[int, int]:
    """
    minimum, maximum = float("inf"), float("-inf")
    with open(file_name) as fp:
        for line in fp:
            number = float(line)
            minimum = number if number < minimum else minimum
            maximum = number if number > maximum else maximum

    return minimum, maximum
