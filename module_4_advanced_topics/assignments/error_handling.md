# Error Handling

## Description
This assignment will introduce you to **error handling** using `try`, `except`, and optionally `finally` and `else` blocks. You will write Python code that anticipates potential issues and responds to them gracefully, without crashing the program.

## Instructions

1. Create a file in your GitHub repository named `error_handling.py`.
2. Complete the following tasks using proper error handling:
    - Write a function called `safe_divide(a, b)` that divides two numbers. If `b` is zero, it should return a helpful message instead of throwing an error.
    - Write a function called `open_file(path)` that tries to open a file and read its contents. If the file doesn’t exist, catch the error and return a helpful message.
    - Write a function called `parse_int_list(strings)` that takes a list of strings and tries to convert them all to integers. If a string cannot be converted, skip it and continue processing the rest.
3. Each function must:
    - Use `try`/`except` blocks to catch errors.
    - Include at least one helpful error message using `print()` or returned strings.
    - Follow PEP 8 and PEP 20 style guidelines.
4. Add, commit, and push your file to GitHub.
5. Submit the URL to your `error_handling.py` file.

## Examples & Test Cases

| Function Call                            | Expected Output                          |
|------------------------------------------|-------------------------------------------|
| `safe_divide(10, 2)`                     | `5.0`                                     |
| `safe_divide(5, 0)`                      | `'Cannot divide by zero'`                |
| `open_file('/tmp/foo.txt')`             | `'Cannot open file: file not found'`     |
| `parse_int_list(['1', 'two', '3'])`     | `[1, 3]`                                  |

## Submission Checklist
- [ ] File named `error_handling.py` created.
- [ ] `safe_divide()` implemented with error handling.
- [ ] `open_file()` implemented with file error handling.
- [ ] `parse_int_list()` implemented with loop and try/except.
- [ ] File pushed to GitHub and URL submitted.

## Grading Criteria

| Criteria                                     | Points |
|----------------------------------------------|--------|
| Correct use of try/except blocks             | 5 pts  |
| All three functions implemented              | 6 pts  |
| Functions return expected results            | 2 pts  |
| Follows style and documentation conventions  | 2 pts  |

**Total**: 15 points

## Resources
- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
