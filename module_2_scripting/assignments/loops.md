# Loops 

## Description
This assignment is designed to help you demonstrate your understanding of different types of loops in Python: `for` loops, `while` loops, and nested loops. You'll write functions to solve various small problems using loops.

## Instructions

1. Create a file named `loops_practice.py` in your GitHub repository.
2. Complete each of the following functions using the appropriate type of loop.
3. Use comments or docstrings to explain what each function is doing.
4. Test your functions with multiple inputs to ensure they work.
5. When you're done, add, commit, push, and submit the GitHub URL of your file.

### Tasks

Implement the following functions in `loops_practice.py`:

```python
def sum_with_for(numbers: list[int]) -> int:
    """Return the sum of a list using a for loop."""
    pass

def count_down_while(start: int) -> list[int]:
    """Return a list counting down from start to 0 using a while loop."""
    pass

def print_grid(rows: int, cols: int) -> None:
    """Print a grid of '*' with the given rows and columns using nested loops."""
    pass

def find_first_even(numbers: list[int]) -> int:
    """Return the first even number in the list using a loop. Return -1 if none found."""
    pass

def reverse_string(s: str) -> str:
    """Return the reverse of the input string using a loop (not slicing)."""
    pass
```

## Examples & Test Cases

| Function Call               | Expected Output               |
|-----------------------------|-------------------------------|
| `sum_with_for([1, 2, 3])`   | `6`                           |
| `count_down_while(5)`       | `[5, 4, 3, 2, 1, 0]`          |
| `print_grid(2, 3)`          | `***\n***`                    |
| `find_first_even([1, 3, 4])`| `4`                           |
| `find_first_even([1, 3, 5])`| `-1`                          |
| `reverse_string("hello")`   | `"olleh"`                     |

## Submission Checklist
- [ ] File `loops_practice.py` created.
- [ ] All five functions implemented using appropriate loop types.
- [ ] Docstrings or comments provided.
- [ ] Functions tested with various inputs.
- [ ] File added, committed, pushed to GitHub.
- [ ] GitHub URL submitted for grading.

## Grading Criteria

| Criteria                                | Points |
|-----------------------------------------|--------|
| Correct use of `for` loop               | 2 pts  |
| Correct use of `while` loop             | 2 pts  |
| Correct use of nested loops             | 3 pts  |
| Each function behaves as expected       | 5 pts  |
| Code includes docstrings or comments    | 2 pts  |
| Code is clean, readable, and formatted  | 1 pt   |

**Total**: 15 points

## Resources
- [loops overview](resources/loops_overview.md)
- [Python Loops Documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
