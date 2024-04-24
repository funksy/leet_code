def decodeString(s):
    stack = []
    result = ""
    count = 0
    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)
        elif char == '[':
            stack.append(count)
            stack.append(result)
            count = 0
            result = ''
        elif char == ']':
            result = stack.pop() + result * stack.pop()
        else:
            result += char
    return result


print(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))