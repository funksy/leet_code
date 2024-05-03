def isIsomorphic(s, t):
    unique_pairs = set(zip(s, t))
    return len(unique_pairs) == len(set(s)) == len(set(t))


s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s, t))