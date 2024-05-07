def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i


nums = [3, 0, 1]
print(missingNumber(nums))