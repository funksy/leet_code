def jump(nums):
    jumps, max_from_pos, max_from_next_pos = 0, 0, 0

    for i in range(len(nums)):
        max_from_next_pos = max(max_from_next_pos, i + nums[i])
        if max_from_next_pos >= len(nums) - 1:
            jumps += 1
            break
        if i == max_from_pos:
            jumps += 1
            max_from_pos = max_from_next_pos
    
    return jumps        



nums = [2,3,1,1,4]
print(jump(nums))