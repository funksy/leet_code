def plusOne(digits):
    i = len(digits) - 1
    
    if digits[i] < 9:
        digits[i] += 1
        return digits
    
    carryover = True
    while i >= 0 and carryover:
        if digits[i] == 9:
            carryover = True
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            carryover = False
    else:
        if carryover:
            digits.insert(0, 1)

    return digits

digits = [1,2,3]
print(plusOne(digits))