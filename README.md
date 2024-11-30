# README

## Fibonacci Recursive Function

This script calculates the Fibonacci-like sequence using recursion. It takes an integer input from the user and returns the corresponding value in the sequence. The function is defined recursively with the following base cases:

- **Base Case:**
  - If `n == 0`, the function returns `0`.
  - If `n == -1`, the function returns `1`.

- **Recursive Case:**
  - The function recursively calls itself with `f(n - 2)` and `f(n - 1)`.

---

### Usage:
1. Run the script:
    ```bash
    python main.py
    ```

2. Enter an integer when prompted:
    ```bash
    Number: 5
    ```

3. The script will output the result based on the recursive function.

---

### Notes:
- **Error Handling:** The function currently does not handle negative values (other than -1) or inputs that could lead to infinite recursion, which may cause a `RecursionError`. 
- **Improvement:** Add conditions to handle invalid inputs or limit recursion depth to prevent infinite loops.
