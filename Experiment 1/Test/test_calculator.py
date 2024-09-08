"""
This module contains test cases for the functions in the calculator module using pytest.

pytest is a framework that makes building simple and scalable test cases easy. 
It supports fixtures, parameterized testing, and a rich set of command-line options.
"""

import pytest
from calculator import add, subtract

# No need to set PYTHONPATH directly in this file; it's managed via the environment.
# However, we would normally ensure that the environment has PYTHONPATH set if needed.
# For example, we can set it in the command line before running pytest:

# Windows:
# set PYTHONPATH=H:\SE Lab\Source Code

# macOS/Linux:
# export PYTHONPATH=H:/SE Lab/Source Code

def test_add():
    """
    Test cases for the add function from the calculator module.

    This test function verifies that the add function correctly computes
    the sum of two numbers.

    It uses the assert statement to check if the output of add() is as expected.
    If an assertion fails, pytest will report it as a failed test.
    """
    # Test cases where the result is positive
    assert add(2, 3) == 5, "Expected 2 + 3 to equal 5"
    # Test cases where the result is zero
    assert add(-1, 1) == 0, "Expected -1 + 1 to equal 0"
    # Test cases where both numbers are zero
    assert add(0, 0) == 0, "Expected 0 + 0 to equal 0"

def test_subtract():
    """
    Test cases for the subtract function from the calculator module.

    This test function verifies that the subtract function correctly computes
    the difference between two numbers.

    It uses the assert statement to check if the output of subtract() is as expected.
    If an assertion fails, pytest will report it as a failed test.
    """
    # Test cases where the result is positive
    assert subtract(5, 3) == 2, "Expected 5 - 3 to equal 2"
    # Test cases where the result is negative
    assert subtract(3, 5) == -2, "Expected 3 - 5 to equal -2"
    # Test cases where both numbers are zero
    assert subtract(0, 0) == 0, "Expected 0 - 0 to equal 0"

# pytest functions:
# - `assert`: Used to assert that a given condition holds true. If the condition is false,
#   pytest will report it as a failure.
# - `pytest` runs all functions prefixed with 'test_' and reports the results.
# - we can run this test file using the command `pytest test_calculator.py` in the terminal.
