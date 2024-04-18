def closeStrings(word1, word2):
    word1_counts, word2_counts = {}, {}
    
    for char in word1:
        if char not in word1_counts:
            word1_counts[char] = 0
        word1_counts[char] += 1
    
    for char in word2:
        if char not in word2_counts:
            word2_counts[char] = 0
        word2_counts[char] += 1

    if sorted(word1_counts.keys()) != sorted(word2_counts.keys()):
        return False
    
    if sorted(word1_counts.values()) != sorted(word2_counts.values()):
        return False
    
    return True


print(closeStrings('baa', 'abb'))