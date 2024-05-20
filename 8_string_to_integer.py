def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    
    res, i, negative = 0, 0, False

    if s[0] == '-':
        i += 1
        negative = True
    
    if s[0] == '+':
        i += 1
    
    while i < len(s):
        if not s[i].isdigit():
            break
        res *= 10
        res += int(s[i])
        i += 1
    
    if negative:
        res *= -1
    if res > 2**31 - 1:
        res = 2**31 - 1
    elif res < -2**31:
        res = -2**31
    
    return res


s = "-4s2"

print(myAtoi(s))