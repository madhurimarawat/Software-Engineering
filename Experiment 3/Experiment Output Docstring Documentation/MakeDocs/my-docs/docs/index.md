# Calculator Class

A simple calculator class to perform basic arithmetic operations.

## Methods

### `add(a, b)`

- **Description**: Returns the sum of two numbers.
- **Parameters**:
  - `a` (int, float): The first number.
  - `b` (int, float): The second number.
- **Returns**:
  - `int` or `float`: The sum of `a` and `b`.
- **Example**:
  ```python
  calc = Calculator()
  result = calc.add(5, 3)  # Returns 8
  ```

### `subtract(a, b)`

- **Description**: Returns the difference when the second number is subtracted from the first number.
- **Parameters**:
  - `a` (int, float): The number to subtract from.
  - `b` (int, float): The number to be subtracted.
- **Returns**:
  - `int` or `float`: The result of `a - b`.
- **Example**:
  ```python
  result = calc.subtract(10, 4)  # Returns 6
  ```

### `multiply(a, b)`

- **Description**: Returns the product of two numbers.
- **Parameters**:
  - `a` (int, float): The first number.
  - `b` (int, float): The second number.
- **Returns**:
  - `int` or `float`: The product of `a` and `b`.
- **Example**:
  ```python
  result = calc.multiply(4, 3)  # Returns 12
  ```

### `divide(a, b)`

- **Description**: Returns the quotient when the first number is divided by the second number. Raises an exception if division by zero is attempted.
- **Parameters**:
  - `a` (int, float): The numerator.
  - `b` (int, float): The denominator.
- **Returns**:
  - `float`: The result of `a / b`.
- **Raises**:
  - `ZeroDivisionError`: If `b` is 0.
- **Example**:
  ```python
  result = calc.divide(10, 2)  # Returns 5.0
  # calc.divide(10, 0)  # Raises ZeroDivisionError
  ```

---

## Usage Example

```python
calc = Calculator()

# Basic Operations
add_result = calc.add(10, 5)         # 15
sub_result = calc.subtract(10, 5)    # 5
mul_result = calc.multiply(10, 5)    # 50
div_result = calc.divide(10, 5)      # 2.0

```

## Experiment

I, Madhurima Rawat (Roll No. 42), am performing a sample experiment related to this MkDocs setup. This project will help me explore how MkDocs generates documentation efficiently.

```

```
