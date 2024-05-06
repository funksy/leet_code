def isValid(s):
    if len(s) < 1:
        return False

    pairs = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif len(stack) == 0 or pairs[stack.pop()] != char:
            return False
    
    return len(stack) == 0
        


s = "()"

print(isValid(s))