#!/usr/bin/env python3


# I have created some functions, but they need your help. Fill out the conditionals to make the
# functions work correctly.


# Here is an example I have filled out for you. Notice how the function must return a value. In this
# case our function returns a bool because it is testing if the number is even.
def is_even(number):
    """
    Tests if the provided number is even or odd.

    :param int number: The number to test.
    :return bool: True if the number is even and false otherwise.
    """
    # This is modular arithmetic. This is testing if the remaider of a number divided by 2 is 0 or
    # not.
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
