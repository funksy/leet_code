def isHappy(n):
    repeat = set()
    while n != 1 and n not in repeat:
        repeat.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return n == 1

n = 2
print(isHappy(n))