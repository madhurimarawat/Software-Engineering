def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    Args:
        n (int): The number to compute factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
