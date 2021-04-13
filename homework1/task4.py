from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    di = {}
    count = 0

    for i in range(len(a)):
        for j in range(len(a)):
            sum = a[i] + b[j]
            if sum in di:
                di[sum] += 1
            else:
                di[sum] = 1

    for k in range (len(a)):
        for l in range (len(a)):
            sum = c[k] + d[l]
            if -sum in di:
                count += di.get(-sum)

    return count

