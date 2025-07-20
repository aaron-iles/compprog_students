# Caesar Cipher – Phase 1: Encrypt

## Description
This is the **first part** of a multi-week project. In this phase, you’ll create a function that implements a **Caesar Cipher** to encrypt a string. Your work now will be reused in future assignments, so follow good coding practices and **be kind to your future self**: write clean, well-documented, readable code!

## Instructions

1. Create a Python file named `cipher.py`.
2. Implement a function called `encrypt()` with the following specification:
    - **Arguments**:
      - `plaintext` (str): the text to encrypt
      - `shift` (int): the number of letters to shift by
    - **Returns**:
      - `str`: the encrypted text (cipher text)
3. Add a `main()` function with the standard Python entry-point check:
    ```python
    if __name__ == '__main__':
        main()
    ```
    Your `main()` function can be empty for now.
4. Follow **PEP 8** and **PEP 20**.
5. Use **type hints** and **docstrings**.
6. Only letters should be shifted; punctuation, spaces, and symbols should remain unchanged.
7. Uppercase and lowercase letters should be handled appropriately and preserved in case.
8. Wrap the shift (e.g., 'Z' shifted by 1 becomes 'A').
9. Submit your file after pushing it to GitHub.

## Hints

- You may find `ord()` and `chr()` useful.
- Use modulo math to wrap the alphabet (26 letters).
- Use separate logic for lowercase and uppercase letters.
- Skip characters that are not alphabetic.

## Examples & Test Cases

| Function Call                                  | Expected Output                        |
|------------------------------------------------|----------------------------------------|
| `encrypt("Hello, World!", 15)`                 | `'wtaad, ldgas!'`                      |
| `encrypt("ABC", 25)`                           | `'zab'`                                |
| `encrypt("Attack at dawn", 19)`                | `'tmmtvd tm wtpg'`                     |
| `encrypt("The lazy brown dog jumps over the fox", 13)` | `'gur ynml oebja qbt whzcf bire gur sbk'` |

## Submission Checklist
- [ ] File `cipher.py` created.
- [ ] `encrypt()` function implemented and working.
- [ ] `main()` function included with entry point.
- [ ] Proper docstrings and type hints added.
- [ ] Code follows PEP 8 and PEP 20.
- [ ] Code committed, pushed, and URL submitted.

## Grading Criteria

| Criteria                                  | Points |
|-------------------------------------------|--------|
| Encrypt function implemented correctly     | 8 pts  |
| Handles upper/lowercase and punctuation    | 3 pts  |
| Wrap-around logic works correctly          | 2 pts  |
| Code is clean, documented, and readable    | 2 pts  |

**Total**: 15 points

## Resources
- [ord() and chr() Functions](https://docs.python.org/3/library/functions.html#ord)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
