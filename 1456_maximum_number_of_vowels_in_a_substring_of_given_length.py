def maxVowels(s, k):
    v = 'aeiou'
    win_vowels = 0
    max_vowels = 0

    for i, char in enumerate(s):
        if i >= k:
            if s[i - k] in v:
                max_vowels -= 1
        if s[i] in v:
            max_vowels += 1
        if max_vowels == k:
            return k
        max_vowels = max(max_vowels, win_vowels)
    return max_vowels

print(maxVowels('leetcode', 3))