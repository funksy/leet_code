from collections import Counter

def isAnagram(s, t):
    return Counter(s).items() == Counter(t).items()

s = 'anagram'
t = 'nagaram'

print(isAnagram(s, t))