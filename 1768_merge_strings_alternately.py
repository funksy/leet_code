def mergeAlternately(word1: str, word2: str) -> str:
    result = ""
    for letter1, letter2 in zip(word1, word2):
        result += letter1 + letter2
    if len(word1) > len(word2):
        result += word1[len(word2):]
    else:
        result += word2[len(word1):]
    return result


print(mergeAlternately("abcd", "pq"))