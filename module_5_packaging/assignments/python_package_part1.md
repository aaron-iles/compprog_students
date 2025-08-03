# Python Package Project - Part 1

## Description
This is the first part of a multi-week project in which you will build a Python package from scratch. You will create a module, structure it properly, and prepare it for building and distribution. This assignment focuses on setting up the initial scaffolding and writing the first piece of functional code.

## Instructions

1. In your GitHub repository, create a directory called `package`. All files related to your package will live inside this directory.
2. Inside the `package` directory:
    - Create a Python module (a `.py` file) that includes the **first function or class** relevant to your package's purpose.
    - Make sure your code follows [PEP 8](https://peps.python.org/pep-0008/) formatting and has appropriate docstrings.
3. Add the necessary configuration files for packaging:
    - `pyproject.toml`
    - `setup.cfg`
    - `tox.ini`
4. Install the required tools to test your package locally:
    ```bash
    python3 -m pip install pytest tox coverage
    ```
5. Run `tox` to ensure your package builds successfully:
    ```bash
    tox
    ```
6. Commit and push your changes to GitHub.
7. Submit a link to the Pull Request (PR) that contains your work.

## Examples & Test Cases

There are no required test cases for this step, but consider writing a simple test file (e.g., `test_example.py`) to verify your function or class behaves as expected.

## Submission Checklist
- [ ] Created a `package` directory.
- [ ] Added an initial module with at least one class or function.
- [ ] Added `pyproject.toml`, `setup.cfg`, and `tox.ini`.
- [ ] Verified package builds successfully using `tox`.
- [ ] Pushed work to GitHub and submitted the PR link.

## Grading Criteria

| Criteria                              | Points |
|---------------------------------------|--------|
| Initial function/class implemented    | 4 pts  |
| PEP 8 and docstring compliance        | 3 pts  |
| All config files created correctly    | 3 pts  |
| Package builds with `tox`             | 3 pts  |
| Code pushed and PR submitted          | 2 pts  |

**Total**: 15 points

## Resources
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Packaging Guide](https://packaging.python.org/en/latest/)
