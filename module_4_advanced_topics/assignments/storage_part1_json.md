# Storage Part 1: JSON

## Description
This assignment introduces students to basic file I/O in Python using the `json` module. You will create a module that includes two functions for reading and writing dictionaries to and from JSON files.

---

## Instructions

1. Create a Python file called `storage_json.py` in your repository.
2. Implement **two functions** inside this file using the provided starter code below:

```python
def read_from_json(path: str) -> dict:
    """
    This function will open and read a JSON file and return the content as a dictionary.
    """

def write_to_json(path: str, content: dict) -> None:
    """
    This function will open and write a dict to a JSON file.
    """
```

3. The `read_from_json()` function should:
   - Take a file path as input
   - Open the file
   - Parse the JSON content and return it as a Python `dict`

4. The `write_to_json()` function should:
   - Take a file path and a `dict` as input
   - Write the dictionary to the file using `json.dump()`
   - Ensure the output is nicely formatted using `indent=4`

5. Use proper **docstrings** and **type hints** for both functions.
6. Follow **PEP 8** and **PEP 20** guidelines.

## Submission Checklist
- [ ] File named `storage_json.py` created
- [ ] Both functions implemented
- [ ] Type hints added for both functions
- [ ] Each function has a proper docstring
- [ ] Code is clean, readable, and PEP 8 compliant
- [ ] File committed and pushed to GitHub
- [ ] GitHub URL submitted

## Grading Criteria

| Criteria                                   | Points |
|--------------------------------------------|--------|
| Correct implementation of `read_from_json` | 5 pts  |
| Correct implementation of `write_to_json`  | 5 pts  |
| Type hints and docstrings included         | 3 pts  |
| Code formatting and readability            | 2 pts  |

**Total**: 15 points

## Resources
- [Python `json` module](https://docs.python.org/3/library/json.html)
- [PEP 8 – Style Guide](https://peps.python.org/pep-0008/)
- [PEP 20 – Zen of Python](https://peps.python.org/pep-0020/)
