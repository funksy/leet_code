def pivotIndex(nums):
    l_sum, r_sum = 0, sum(nums)
    for i, num in enumerate(nums):
        r_sum -= num
        if l_sum == r_sum:
            return i
        l_sum += num
    return -1



print(pivotIndex([2,1,-1]))