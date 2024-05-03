from collections import Counter

def canConstruct(ransomNote, magazine):
    magazine = Counter(magazine)
    for char in ransomNote:
        if char not in magazine or magazine[char] < 1:
            return False
        magazine[char] -= 1
    return True


ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))