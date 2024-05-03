def canJump(nums):
    target = len(nums) - 1
    nums[-1] = True

    for i in range(len(nums) - 1, -1, -1):      
        if nums[i] >= target - i:
            nums[i] = True
            target = i
        else:
            nums[i] = False
    
    return nums[0]
        



print(canJump([2,3,1,1,4]))