def lengthOfLastWord(s):
    s = s.rstrip().rsplit(' ', maxsplit=1)
    return len(s[-1])


s = "Hello World"
print(lengthOfLastWord(s))