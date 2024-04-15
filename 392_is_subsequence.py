def isSubsequence(s, t):
    len_s, len_t = len(s), len(t)
    i, j = 0, 0
    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len_s



print(isSubsequence('abc', 'abfdc'))
