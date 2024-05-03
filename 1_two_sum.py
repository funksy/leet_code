def twoSum(nums, target):
    pair = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in pair:
            return [pair[diff], i]
        else:
            pair[nums[i]] = i