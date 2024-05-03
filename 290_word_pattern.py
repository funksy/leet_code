def wordPattern(pattern, s):
    s = s.split(' ')
    if len(s) != len(pattern):
        return False

    pattern_set = set(pattern)
    s_set = set(s)
    zip_set = set(zip(pattern, s))

    return len(pattern_set) == len(s_set) == len(zip_set)


pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern, s))