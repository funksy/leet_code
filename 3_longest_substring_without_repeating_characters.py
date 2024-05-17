def lengthOfLongestSubstring(s):
    chars = set()
    max_length, left = 0, 0

    for right in range(len(s)):
        if s[right] not in chars:
            chars.add(s[right])
            max_length = max(max_length, right- left + 1)
        else:
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
    
    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))