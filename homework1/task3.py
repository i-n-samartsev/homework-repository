from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        new_list = []
        for line in fi:
            value = int(line)
            new_list.append(value)
        minimum = min(new_list)
        maximum = max(new_list)
        return minimum, maximum
