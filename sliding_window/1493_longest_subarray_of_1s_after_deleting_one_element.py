def longestSubarray(nums):
    start_win, zeroes = 0, 0
    for end_win in range(len(nums)):
        if nums[end_win] == 0:
            zeroes += 1
        if zeroes > 1:
            if nums[start_win] == 0:
                zeroes -= 1
            start_win += 1
    return end_win - start_win


test1 = [1,1,0,1]
test2 = [0,1,1,1,0,1,1,0,1]
test3 = [1, 1, 1]

print(longestSubarray(test1))
print(longestSubarray(test2))
print(longestSubarray(test3))