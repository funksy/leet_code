def generate(numRows):
    rows = [[1]]

    while len(rows) < numRows:
        i = 0
        newRow = [1]
        for j in range(len(rows[-1]) - 1):
            newRow.append(rows[-1][j] + rows[-1][j + 1])
        else:
            newRow.append(1)
        rows.append(newRow)
        i += 1

    return rows


print(generate(6))