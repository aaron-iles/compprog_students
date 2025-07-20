# Executing Files

## Description
We won’t be using IDEs for programming in this class. We will be using the true engineer’s method: text files. Python scripts are just simple text files and they are executed using the system’s Python interpreter. You can create a Python script from the command line or from the GUI. Below is an example of how to create a Python script.

## Instructions

1. Create an empty file by using the `touch` command:
    ```bash
    cd /tmp
    touch my_script.py
    ```

2. Use `cat` to read the file (it should be empty):
    ```bash
    cat my_script.py
    ```

3. Make the script executable using `chmod`:
    ```bash
    chmod 770 my_script.py
    ```

4. Run the (empty) script using Python:
    ```bash
    python3 my_script.py
    ```

5. Open the file in Sublime:
    ```bash
    subl my_script.py
    ```

6. Add the following code and save the file:
    ```python
    print("Hello World!")
    ```

7. Exit Sublime and run the script again:
    ```bash
    python3 my_script.py
    ```

8. Did you see "Hello World!" printed in the terminal? If not, raise your hand.

9. Add a **shebang** line to the top of the file so it can be run directly:
    ```python
    #! /usr/bin/env python3
    print("Hello World!")
    ```

10. Make sure the file is still executable, then run it using:
    ```bash
    ./my_script.py
    ```

## Examples & Test Cases

| Command               | Expected Output   |
|----------------------|-------------------|
| `cat my_script.py`   | *(shows code)*    |
| `python3 my_script.py` | `Hello World!`  |
| `./my_script.py`     | `Hello World!`    |

## Submission Checklist
- [ ] Created a Python script using `touch`.
- [ ] Viewed and edited the file.
- [ ] Made the file executable using `chmod`.
- [ ] Ran the script using both `python3` and `./` with shebang.
- [ ] Confirmed that "Hello World!" was printed to the terminal.

## Grading Criteria

| Criteria                            | Points |
|-------------------------------------|--------|
| Script created and edited properly  | 5 pts  |
| Script ran with Python interpreter  | 5 pts  |
| Script executed using shebang       | 5 pts  |

**Total**: 15 points

## Resources
- [Bash Cheat Sheet](../resources/bash_cheat_sheet.sh)
