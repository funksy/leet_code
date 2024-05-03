def increasingTriplet(nums):
    first, second = float('inf'), float('inf')
    for third in nums:
        if first <= third:
            first = third
        elif second <= third:
            second = third
        else:
            return True
    return False