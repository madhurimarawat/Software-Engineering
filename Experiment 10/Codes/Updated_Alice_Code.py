def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate factorial for. Must be non-negative.

    Returns:
        int: The factorial of the number.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
