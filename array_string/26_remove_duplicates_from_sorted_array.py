def removeDuplicates(nums):
    index, unique_element = 0, nums[0]
    for i in range(len(nums)):
        if nums[i] != unique_element:
            nums[index + 1] = nums[i]
            unique_element = nums[index + 1]
            index += 1
    return index + 1


nums = [0,0,1,1,1,2,2,3,3,4]

print(nums[:removeDuplicates(nums)])