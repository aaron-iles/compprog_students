# Hello $USER

## Description
For this assignment, you will create a "Hello, World!" style script in Python. The script must greet the user running it by name and must be named `hello_user.py`. When you're finished, make sure to **add**, **commit**, **push**, and **submit the URL** of the file in your GitHub repository.

## Instructions

- Create a Python script named `hello_user.py`.
- The script should print:
  ```
  Hello <username>
  ```
  where `<username>` is dynamically obtained based on the user running the script. **Hard-coding a name is not allowed.**
- Follow these additional steps for extra credit:
  - **+1 point**: Add helpful comments or a docstring to explain the purpose of the script.
  - **+1 point**: Follow [PEP 8](https://peps.python.org/pep-0008/) formatting standards (e.g., clear variable names, consistent indentation, spacing).
  - **+1 point**: Use the `if __name__ == '__main__':` convention to run your code.

Use Google to look up any of these requirements, and don't hesitate to ask questions if you’re stuck.

## Examples & Test Cases

| Command                      | Expected Output           |
|-----------------------------|---------------------------|
| `python3 hello_user.py`     | `Hello aaron` *(or user)* |

## Submission Checklist
- [ ] Script prints `Hello <username>` based on the current user.
- [ ] Script is named `hello_user.py`.
- [ ] Script was added, committed, and pushed to your GitHub repo.
- [ ] Submitted the URL to your file in GitHub.
- [ ] (Optional) Added comments/docstring.
- [ ] (Optional) Followed PEP 8 standards.
- [ ] (Optional) Used `if __name__ == '__main__':`.

## Grading Criteria

| Criteria                                   | Points |
|--------------------------------------------|--------|
| Script prints dynamic username              | 5 pts  |
| Helpful comments or docstring               | +1 pt  |
| PEP 8 style formatting                      | +1 pt  |
| Used `if __name__ == '__main__':`          | +1 pt  |

**Total**: Up to 8 points

## Resources
- [Python PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Getting the Current Username in Python](https://docs.python.org/3/library/getpass.html)
