def longestPalindrome(s):
    longest_p = s[0]

    for i in range(len(s) - 1):
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(s[left + 1:right]) > len(longest_p):
            longest_p = s[left + 1:right]
        
        left = i
        right = i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(s[left + 1:right]) > len(longest_p):
            longest_p = s[left + 1:right]
    
    return longest_p

s = "cbbd"
print(longestPalindrome(s))