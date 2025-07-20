# Conditionals

## Description
Exercise your understanding of conditionals by completing partially written functions. You'll practice using `if`, `elif`, and `else` statements in Python.

## Instructions

1. Create a file in your GitHub repository named `conditionals.py`.
2. Copy and paste the following starter code into your file:
    ```python
    #!/usr/bin/env python3

    # Here is an example I have filled out for you. Notice how the function must return a value. In this
    # case our function returns a bool because it is testing if the number is even.
    def is_even(number):
        """
        Tests if the provided number is even or odd.

        :param int number: The number to test.
        :return bool: True if the number is even and false otherwise.
        """
        if number % 2 == 0:
            return True
        else:
            return False

    def calculate_grade(numeric_grade):
        """
        This function will calculate the letter grade for a student given the numeric grade.
        90 - 100 -> A
        80 - 89 -> B
        70 - 79 -> C
        60 - 69 -> D
        0 - 59 -> F

        :param int numeric_grade: The numeric grade of a student.
        :return str: The letter grade (A-F) for the student.
        """
        # TODO: Fill this out.

    def age_classifier(age):
        """
        This function will classify an individual as "child", "adult", or "teenager" based on their age.

        :param int age: The age of the individual in years.
        :return str: The person's classification. Either "child", "adult", or "teenager".
        """
        # TODO: Fill this out.
    ```

3. Complete the `calculate_grade` and `age_classifier` functions using conditional logic.
4. Make sure each function returns the correct type and behaves as expected.
5. Add, commit, and push your file to GitHub.
6. Submit the URL to your `conditionals.py` file.

## Examples & Test Cases

| Function Call            | Expected Output |
|--------------------------|-----------------|
| `is_even(4)`             | `True`          |
| `is_even(5)`             | `False`         |
| `calculate_grade(95)`    | `'A'`           |
| `calculate_grade(72)`    | `'C'`           |
| `calculate_grade(50)`    | `'F'`           |
| `age_classifier(10)`     | `'child'`       |
| `age_classifier(16)`     | `'teenager'`    |
| `age_classifier(25)`     | `'adult'`       |

## Submission Checklist
- [ ] File named `conditionals.py` created.
- [ ] `calculate_grade()` function implemented correctly.
- [ ] `age_classifier()` function implemented correctly.
- [ ] Code returns expected results for all test cases.
- [ ] File pushed to GitHub and URL submitted.

## Grading Criteria

| Criteria                                     | Points |
|----------------------------------------------|--------|
| Correct implementation of `calculate_grade`  | 5 pts  |
| Correct implementation of `age_classifier`   | 5 pts  |
| Code returns expected results                | 3 pts  |
| Follows style and documentation conventions  | 2 pts  |

**Total**: 15 points

## Resources
- [Conditionals Overview](../resources/conditionals_overview.md)
