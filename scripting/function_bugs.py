#!/usr/bin/env python3


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

# Test the function
numbers = [10, 15, 20, 25, 30]
result = calculate_average(numbers)
print(f"The average is: {result}")


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

# Test the function
numbers = [5, 10, 3, 8, 15]
result = find_largest_number(numbers)
print(f"The largest number is: {result}")


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

# Test the function
word = "Python"
result = count_vowels(word)
print(f"The number of vowels in '{word}' is: {result}")
