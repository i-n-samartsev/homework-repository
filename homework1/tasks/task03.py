from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    value = []
    with open(file_name + ".txt") as fi:
        for line in fi:
            value.append(int(line))
    return min(value), max(value)
