def searchInsert(nums, target):
    i = 0
    
    while i < len(nums):
        if nums[i] >= target:
            return i
        i += 1
    return i


nums = [1,3,5,6]
target = 5

print(searchInsert(nums, target))