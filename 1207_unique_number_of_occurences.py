def uniqueOccurences(arr):
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    unique = []
    for _, val in counts.items():
        if(val in unique):
            return False
        else:
            unique.append(val)
    return True


print(uniqueOccurences([-3,0,1,-3,1,1,1,-3,10,0]))