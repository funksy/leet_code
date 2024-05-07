def getRow(rowIndex):
    row = [1]

    while len(row) < rowIndex + 1:
        i = 0
        newRow = [1]
        for j in range(len(row) - 1):
            newRow.append(row[j] + row[j + 1])
        else:
            newRow.append(1)
        row = newRow
        i += 1

    return row


print(getRow(1))