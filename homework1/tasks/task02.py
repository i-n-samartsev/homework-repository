from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 2:
        return False
    if data[0] == 0 and data[1] == 1:
        for i in range(0, len(data) - 2):
            if data[i] + data[i + 1] != data[i + 2]:
                return False
    return True
