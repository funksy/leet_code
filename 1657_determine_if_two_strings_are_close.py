from collections import Counter

def closeStrings(word1, word2):
    word1_counts = Counter(word1)
    word2_counts = Counter(word2)
    
    if sorted(word1_counts.keys()) != sorted(word2_counts.keys()):
        return False
    if sorted(word1_counts.values()) != sorted(word2_counts.values()):
        return False
    return True


print(closeStrings('baa', 'abb'))