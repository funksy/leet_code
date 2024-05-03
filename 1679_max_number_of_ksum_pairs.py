def maxOperations(nums, k):
    if len(nums) < 2:
        return 0
    
    nums.sort()
    first, second, count = 0, len(nums) - 1, 0

    while second < len(nums) and first < second:
        if nums[second] < k - nums[first]:
            first += 1
        elif nums[second] > k - nums[first]:
            second -= 1
        else:
            count += 1
            first += 1
            second -= 1
        
    return count



test1list = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
test1k = 2

test2list = [1,2,3,4]
test2k = 5

print(maxOperations(test1list, test1k))
print(maxOperations(test2list, test2k))