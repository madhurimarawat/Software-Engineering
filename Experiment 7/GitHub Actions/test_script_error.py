# test_script_error.py

# Import the functions to be tested from script.py
from script import add, subtract


# Function to test the add function
def test_add():
    # Check if adding 3 and 2 equals 5
    assert add(3, 2) == 5  # This will pass


# Function to test the subtract function
def test_subtract():
    # Check if subtracting 2 from 5 equals 4
    assert subtract(5, 2) == 4  # This will fail
