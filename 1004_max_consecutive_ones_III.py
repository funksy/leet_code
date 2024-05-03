def longestOnes(nums, k):
    zeros, start_win = 0, 0
    for end_win in range(len(nums)):
        if nums[end_win] == 0:
            zeros += 1
        if zeros > k:
            if nums[start_win] == 0:
                zeros -= 1
            start_win += 1
    return end_win - start_win + 1


test1 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
test1k = 3

test2 = [1,1,1,0,0,0,1,1,1,1,0]
test2k = 2

print(longestOnes(test1, test1k))
print(longestOnes(test2, test2k))