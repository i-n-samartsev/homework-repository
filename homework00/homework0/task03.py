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


def flatten(lines):
    return [item for sublist in lines for item in sublist]


def read_file(file_name: str) -> list:
    lines = []
    with open(file_name) as f:
        for line in f:
            lines.append(list(map(int, line.split())))
    print(flatten(lines))
    """
    np.ndarray.flatten sometimes returns same list -> good old hand flatten

    """
    return flatten(lines)


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    lines = read_file(file_name)
    return (min(lines), max(lines))
