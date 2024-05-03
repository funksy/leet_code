def longestCommonPrefix(strs):
    longest_pre = ''
    strs.sort()

    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            longest_pre += strs[0][i]
        else:
            return longest_pre
    
    return longest_pre


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))