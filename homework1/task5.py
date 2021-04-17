def find_maximal_subarray_sum(nums, k) -> int:
    sub_arrays = []
    list_of_sums = []

    for i in range(len(nums) - 1):
        sub_arrays.append((nums[i]))
        sub_arrays.append(nums[i:i + k])
        sub_arrays.append(nums[i:i - k])
    sub_arrays[-1].append(nums[-1])

    for i in sub_arrays:
        if type(i) == list:
            list_of_sums.append(sum(i))
        else:
            list_of_sums.append(i)
        maximum = max(list_of_sums)

    return maximum
