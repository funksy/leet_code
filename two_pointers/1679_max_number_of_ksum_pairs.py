def maxOperations(nums, k):
    if len(nums) < 2:
        return 0

    first, count = 0, 0
    flag = True

    while flag == True:
        flag = False
        if nums:
            search_num = k - nums[first]

            if search_num in nums[first:]:
                print('nums: ', nums)
                print('search_num: ', search_num)
                print('first num: ', nums[first])
                count += 1
                nums.remove(nums[first])
                nums.remove(search_num)
                flag = True
            
            elif first < len(nums) - 1:
                flag = True
                first += 1

    return count



test1list = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
test1k = 2

test2list = [3,1,3,4,3]
test2k = 6

print(maxOperations(test1list, test1k))
print(maxOperations(test2list, test2k))