# Function Bugs

## Description
The following Python script contains three functions. Each appears to work at first glance, but each has a subtle bug that needs fixing. Your job is to identify and correct the bugs using your knowledge of testing and debugging.

## Instructions

1. Copy the three functions below into a file in your GitHub repository named `function_bugs.py`.
2. Write test cases to try each function with **different types of input**, including edge cases.
3. Identify the bug(s) in each function and implement a fix.
4. When you're done, `git add`, `commit`, and `push` your changes to your repository.
5. Submit the URL of the file from your GitHub repo.

### Starter Code

```python
# Exercise 1
def calculate_average(numbers: list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - numbers (list): A list of numerical values.

    Returns:
    - float: The average of the input numbers. Returns 0 if the list is empty.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average


# Exercise 2
def find_largest_number(numbers: list) -> int:
    """
    Find the largest number in a list.

    Parameters:
    - numbers (list): A list of numerical values.

    Returns:
    - int or None: The largest number in the list. Returns None for an empty list.
    """
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# Exercise 3
def count_vowels(word: str) -> int:
    """
    Count the number of vowels in a given word (case-insensitive).

    Parameters:
    - word (str): The input word.

    Returns:
    - int: The number of vowels in the word.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count
```

## Examples & Test Cases

You should test each function with:
- An empty list
- Negative numbers
- Edge cases (e.g., only one item in the list)
- Uppercase/lowercase inputs

| Function Call                    | Expected Outcome               |
|----------------------------------|--------------------------------|
| `calculate_average([])`         | `0.0`                          |
| `find_largest_number([-3, -1])` | `-1`                           |
| `count_vowels("HELLO")`         | `2`                            |

## Submission Checklist
- [ ] Created `function_bugs.py` in your GitHub repo.
- [ ] Tested each function with a variety of inputs.
- [ ] Fixed all three bugs.
- [ ] Pushed the updated file to GitHub.
- [ ] Submitted the GitHub URL.

## Grading Criteria

| Criteria                              | Points |
|---------------------------------------|--------|
| Bug fixed in `calculate_average()`    | 4 pts  |
| Bug fixed in `find_largest_number()`  | 4 pts  |
| Bug fixed in `count_vowels()`         | 3 pts  |
| Clear and valid test cases used       | 2 pts  |
| Code formatting and clarity           | 2 pts  |

**Total**: 15 points

## Resources
- [Python Testing Basics](https://realpython.com/python-testing/)
