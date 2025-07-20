# Caesar Cipher – Phase 2: Decrypt

## Description
In this phase of the multi-week Caesar Cipher project, you will write a **decrypt** function that reverses the Caesar Cipher transformation. This function will allow you to recover the original message from encrypted text using the correct shift value.

You will also combine this function with your `encrypt()` function in the same Python module (`cipher.py`).

## Instructions

1. Continue working in your existing `cipher.py` file.
2. Implement a function called `decrypt()` with the following specification:
    - **Arguments**:
      - `ciphertext` (str): the encrypted message
      - `shift` (int): the Caesar Cipher shift used during encryption
    - **Returns**:
      - `str`: the decrypted original message (plain text)
3. Your decrypt function should reverse the shift logic used in your `encrypt()` function.
4. Preserve case sensitivity and leave punctuation/symbols unchanged.
5. Use proper **docstrings** and **type hints**.
6. Ensure that your code continues to follow **PEP 8** and **PEP 20**.
7. You may include code to test encryption and decryption in your `main()` function.

## Examples & Test Cases

| Function Call                                       | Expected Output          |
|----------------------------------------------------|--------------------------|
| `decrypt("wtaad, ldgas!", 15)`                     | `'hello, world!'`        |
| `decrypt("zab", 25)`                               | `'abc'`                  |
| `decrypt("tmmtvd tm wtpg", 19)`                    | `'attack at dawn'`       |
| `decrypt("gur ynml oebja qbt whzcf bire gur sbk", 13)` | `'the lazy brown dog jumps over the fox'` |

## Submission Checklist
- [ ] `cipher.py` includes both `encrypt()` and `decrypt()` functions.
- [ ] Both functions have appropriate docstrings and type hints.
- [ ] Decryption logic mirrors and reverses the encryption logic.
- [ ] Case, punctuation, and symbols are handled correctly.
- [ ] Code is clean and documented.
- [ ] File added, committed, and pushed to GitHub.
- [ ] GitHub URL submitted.

## Grading Criteria

| Criteria                                   | Points |
|--------------------------------------------|--------|
| Decrypt function implemented correctly      | 8 pts  |
| Case and punctuation preserved properly     | 3 pts  |
| Reverses encryption accurately              | 2 pts  |
| Docstrings, type hints, and PEP compliance  | 2 pts  |

**Total**: 15 points

## Resources
- [ord() and chr() Functions](https://docs.python.org/3/library/functions.html#ord)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
