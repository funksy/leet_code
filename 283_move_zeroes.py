def moveZeroes(nums):
    point1 = 0
    for point2 in range(len(nums)):
        if nums[point2] != 0 and nums[point1] == 0:
            nums[point1], nums[point2] = nums[point2], nums[point1]
        if nums[point1] != 0:
            point1 += 1
    print(nums)


moveZeroes([0,1,2,0,3])