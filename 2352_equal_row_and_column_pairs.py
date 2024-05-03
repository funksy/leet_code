from collections import Counter

def equalPairs(grid):
    result = 0
    row_hash = Counter(tuple(row) for row in grid)
    for column_hash in zip(*grid): # '*' is the unpacking operator, so this effectively "unzips" the grid
        result += row_hash[column_hash]
    return result


print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))