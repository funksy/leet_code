def hIndex(citations):
    citations.sort()
    n = len(citations)
    print(n)

    for i, count in enumerate(citations):
        if n - i <= count:
            return n - i
    
    return 0


citations = [3, 0, 6, 1, 5]

print(hIndex(citations))