# Function Bugs

## Description
In the code below there are 3 functions. Each of them appears to work well, but they each have a bug that needs fixing. I did not give you the test cases that will actually cause them to break-- it is up to you to find the bugs.

## Instructions
1. Copy the functions below into a file in your repo so you can test and fix them.
2. Try running the functions with a few different test cases to see if you can identify the bug in each function.
3. Once you have identified the bug, implement a fix.
4. git add, commit, and push!
5. Submit a link to the file in your repo.

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
