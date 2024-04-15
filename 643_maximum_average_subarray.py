def findMaxAverage(nums, k):
    current = highest = sum(nums[:k])
    for i in range(len(nums) - k):
        current += nums[i + k] - nums[i]
        highest = max(current, highest)
    return highest / k



print(findMaxAverage([1,12,-5,-6,50,3], 4))