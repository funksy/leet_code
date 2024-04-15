def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    list_vowels = []
    result = ''
    for char in s:
        if char in vowels:
            list_vowels.append(char)
    for i in range(len(s)):
        if s[i] in vowels:
            result += list_vowels.pop()
        else:
            result += s[i]
    return result


print(reverseVowels("leetcode"))