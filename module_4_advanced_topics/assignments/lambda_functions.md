# Lambda Practice

## Description
Practice using `lambda` functions with `map()` and `filter()` in Python. You will create small, testable expressions that transform and filter data using functional programming techniques.

## Instructions

1. Create a file in your GitHub repository named `m3a0.py`.
2. Complete each of the following tasks using `lambda` functions and either `map()` or `filter()`:

```python
# 1. Write a filter with a lambda that removes values greater than 5 from a list.
# 2. Write a map with a lambda that squares each value in a list.
# 3. Write a map with a lambda that appends ".com" to each string in a list.
# 4. Write a filter with a lambda that keeps only strings of length 1.
# 5. Write a filter with a lambda that removes all dictionaries from the list below
#    that do not contain the "name" key.

data = [
    {
        "name": "Isaiah",
        "enrolled": True
    },
    {
        "name": "Shaedon",
        "assigned": False
    },
    {
        "is_cat": True,
        "pet_name": "Rudy"
    },
    {
        "id": "Jordan",
        "number": 19
    }
]
```

3. Save and test your script.
4. Add, commit, and push your file to GitHub.
5. Submit the URL to your `m3a0.py` file.

## Examples & Test Cases

| Task                                      | Example Input           | Expected Output                  |
|-------------------------------------------|--------------------------|----------------------------------|
| Filter values > 5                         | `[1, 6, 2, 9]`           | `[1, 2]`                         |
| Square values                             | `[2, 3, 4]`              | `[4, 9, 16]`                     |
| Append `.com`                             | `["foo", "bar"]`         | `["foo.com", "bar.com"]`        |
| Filter by string length == 1              | `["a", "hi", "z"]`       | `["a", "z"]`                     |
| Filter dicts missing "name"               | See `data` above         | Only dicts with `"name"` key    |

## Submission Checklist
- [ ] File named `m3a0.py` created.
- [ ] All five tasks completed using `lambda` functions.
- [ ] Code tested and produces the expected output.
- [ ] File committed and pushed to GitHub.
- [ ] GitHub URL submitted.

## Grading Criteria

| Criteria                                      | Points |
|-----------------------------------------------|--------|
| Correct use of lambda in all 5 tasks           | 10 pts |
| File named and submitted correctly             | 2 pts  |
| Output is accurate and testable                | 2 pts  |
| Code formatting and readability                | 1 pt   |

**Total**: 15 points

## Resources
- [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [map() and filter()](https://docs.python.org/3/library/functions.html#map)
