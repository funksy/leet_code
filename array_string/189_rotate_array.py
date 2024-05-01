def rotate(nums, k):
    if k > len(nums):
        nums[:] = rotate(nums, k - len(nums))
    
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

nums = [1, 2]
k = 3

rotate(nums, 3)
print(nums)