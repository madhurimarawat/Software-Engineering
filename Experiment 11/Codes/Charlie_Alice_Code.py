def palindrome(s):
    s = "".join(s.split()).lower()
    return s == s[::-1]
