def reverseWords(s):
    return " ".join([w for w in reversed(s.split(" ")) if w != '']).strip