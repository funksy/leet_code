def isPalindrome(x):
    x = str(x)
    return x == x[::-1]


x = 121
print(isPalindrome(x))