def threeSum(nums):
    triplets = set()

    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        first = nums[i]

        while j < k:
            second = nums[j]
            third = nums[k]
            total = first + second + third
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                triplets.add((first, second, third))
                while j < k and nums[j] == second:
                    j += 1
                while j < k and nums[k] == third:
                    k -= 1

    return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))