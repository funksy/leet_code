def strStr(haystack, needle):
    win_size = len(needle)
    if win_size > len(haystack):
        return -1
        
    for i in range(len(haystack) - win_size + 1):
        if haystack[i:i + win_size] == needle:
            return i
    
    return -1

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))