def removeStars(s):
    stack = []
    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


print(removeStars("erase*****"))