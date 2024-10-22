class Calculator:
    """
    A simple calculator class to perform basic operations.

    Methods
    -------
    add(a, b)
        Adds two numbers.
        
    subtract(a, b)
        Subtracts second number from first number.
        
    multiply(a, b)
        Multiplies two numbers.
        
    divide(a, b)
        Divides first number by second number. Raises ZeroDivisionError for division by zero.
    """
    
    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Returns the difference when b is subtracted from a."""
        return a - b
    
    def multiply(self, a, b):
        """Returns the product of a and b."""
        return a * b
    
    def divide(self, a, b):
        """
        Returns the quotient of a divided by b.

        Raises
        ------
        ZeroDivisionError
            If b is 0.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b
