def check_palindrome(string):
    return string.replace(" ", "").lower() == string.replace(" ", "").lower()[::-1]
