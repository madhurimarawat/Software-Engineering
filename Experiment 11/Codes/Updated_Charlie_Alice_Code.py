def is_palindrome(s: str) -> bool:
    """
    Verify if the input string is a palindrome, ignoring spaces and case.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = "".join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]
