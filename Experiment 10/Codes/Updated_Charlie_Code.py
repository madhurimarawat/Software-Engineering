def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return 1 if n == 0 else n * factorial(n - 1)
