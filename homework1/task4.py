from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    dict = {}
    count = 0

    for i in range(len(a)):
        for j in range(len(a)):
            summa = a[i] + b[j]
            if summa in dict:
                dict[summa] += 1
            else:
                dict[summa] = 1

    for k in range(len(a)):
        for l in range(len(a)):
            summa = c[k] + d[l]
            if -summa in dict:
                count += dict.get(-summa)

    return count

