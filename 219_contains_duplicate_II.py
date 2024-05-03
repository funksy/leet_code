def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and abs(i - seen[num]) <= k:
            return True
        else:
            seen[num] = i
    return False


nums = [1,2,3,1,2,3]
k = 2

print(containsNearbyDuplicate(nums, k))
