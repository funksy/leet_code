def guessNumber(n):
    lower, upper = 1, n

    while lower <= upper:
        mid = lower + (upper - lower) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:
            upper = mid - 1
        else:
            lower = mid + 1