# Calculator

## Description
For this assignment, you will create a **module** (a single Python file) named `calculator.py` that contains four functions: `add`, `subtract`, `multiply`, and `divide`.

## Instructions

1. Create a Python file named `calculator.py` in your GitHub repository.
2. Define four functions in the file: `add`, `subtract`, `multiply`, and `divide`.
3. Each function should:
   - Accept **exactly two arguments**.
   - Use descriptive parameter names.
   - Return the correct result of the operation.
   - Handle errors gracefully (e.g., division by zero).
   - Be written using [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
   - Follow the spirit of [PEP 20](https://peps.python.org/pep-0020/) ("The Zen of Python").
   - Include a docstring explaining what the function does.
   - Use Python **type hints** for both input arguments and return values.

This assignment will be graded as we cover different concepts, so focus on good structure and clarity from the start.

## Examples & Test Cases

| Function Call              | Expected Output |
|---------------------------|-----------------|
| `add(3, 4)`                | `7`             |
| `subtract(10, 4)`          | `6`             |
| `multiply(3, 5)`           | `15`            |
| `divide(10, 2)`            | `5.0`           |
| `divide(10, 0)`            | Graceful error  |

## Submission Checklist
- [ ] Script is named `calculator.py`.
- [ ] Contains all four functions.
- [ ] Each function has a descriptive name and arguments.
- [ ] Syntax is valid and functional.
- [ ] Type hints are used for all function arguments and return values.
- [ ] Each function includes a docstring.
- [ ] Code follows PEP 8 formatting.
- [ ] Code reflects PEP 20 principles.
- [ ] File was added, committed, and pushed to GitHub.
- [ ] GitHub URL was submitted.

## Grading Criteria

| Criteria                                      | Points |
|-----------------------------------------------|--------|
| Four functions are present and correct         | 4 pts  |
| Functions run without syntax errors            | 2 pts  |
| Arithmetic operations return correct results   | 2 pts  |
| Follows PEP 20 philosophy                      | 1 pt   |
| Follows PEP 8 formatting                       | 1 pt   |
| Functions include meaningful docstrings        | 2 pts  |
| Type hints included for all args and returns   | 3 pts  |

**Total**: 15 points

## Resources
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
- [good example code](../resources/good_example_code.py)
