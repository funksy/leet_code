def largestAltitude(gain):
    curr, highest = 0, 0
    for num in gain:
        curr += num
        highest = max(curr, highest)
    return highest


print(largestAltitude([-4,-3,-2,-1,4,3,2]))