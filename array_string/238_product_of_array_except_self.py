def productExceptSelf(nums):
    if nums.count(0) > 1:
        return [0] * len(nums)

    res = [1] * len(nums)

    left, right = 1, 1
    for i in range(len(nums)):
        res[i] = left
        left *= num[i]
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    
    return res