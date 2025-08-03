# Python Package Unit Tests

## Description
In this assignment, you will write at least one **meaningful** unit test for the Python package you have been building. The test should target some real functionality in your code and demonstrate correctness. You will run `tox` to ensure everything works as expected.

## Instructions

1. Create a test module inside your `package/tests/` directory (if it does not already exist).
2. Write at least **one** unit test that meaningfully tests the functionality of your package.
3. Run the test using `tox` and verify that it passes.
4. Ensure your test(s) are discoverable by `pytest` and included in your `tox.ini` config.
5. Commit your changes and push them to the **main** branch.
6. Submit the URL to your GitHub repository where the test can be found.

## Examples & Test Cases

Suppose your package contains a function `add(x, y)` in a module named `math_utils.py`. A simple test could be:

```python
from package.math_utils import add

def test_add_positive_numbers():
    assert add(2, 3) == 5
```

## Submission Checklist

- [ ] Created a test file inside `package/tests/`.
- [ ] Wrote at least one meaningful unit test.
- [ ] Verified tests run successfully using `tox`.
- [ ] Committed and pushed the changes to your main branch.
- [ ] Submitted the link to the test file in your GitHub repo.

## Grading Criteria

| Criteria                                 | Points |
|------------------------------------------|--------|
| Meaningful unit test provided            | 5 pts  |
| Test passes using `tox`                  | 3 pts  |
| Follows PEP 8 and is readable            | 2 pts  |

**Total**: 10 points

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [tox documentation](https://tox.readthedocs.io/)
