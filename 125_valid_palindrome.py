def isPalindrom(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrom(s))