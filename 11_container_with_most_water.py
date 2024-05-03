def maxArea(height):
    left, right = 0, len(height) - 1
    res = 0

    while left < right:
        w = right - left
        if min(height[left], height[right]) * w > res:
            res = min(height[left], height[right]) * w
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return res

test1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(test1))