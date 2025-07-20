#! /usr/bin/env python3


import getpass
import math


def is_prime(n: int) -> bool:
    """
    This function determines whether the provided number, n, is prime.

    :param int n: A number to test primality.
    :return bool: True if the number is prime, False otherwise.
    """
    # If the arg passed is not an int, return False.
    if type(n) != int:
        return False
    # Test the basic cases first.
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    # For all ints greater than 2, exhaust all values up to the square root of n + 1.
    sqrt_n = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True


def say_my_name() -> None:
    """
    This function prints the name of the user running the script.

    :return None:
    """
    print(f"Your name is {getpass.getuser()}")
    return


def str_to_list(delimited_string: str, delimiter: str) -> list:
    """
    This function splits a string into a list based on a given delimiter.
    >>> str_to_list('a,b,c', ',')
        ['a', 'b', 'c']

    :param str delimited_string: The string to be split into a list.
    :param str delimiter: The delimiter on which to split the string.
    :return list: A list of strings as a result of the split.
    """
    if type(delimited_string) != type(delimiter) != str:
        print("ERROR: inputs must be strings")
        return []
    if delimiter not in delimited_string:
        print(f"WARNING: the provided string does not contain the delimiter <{delimiter}>")
    return delimited_string.split(delimiter)


def main():
    say_my_name()
    result_is_prime = is_prime(101)
    name_list = str_to_list("Butler,Jiggs,Scout", ",")
    return


if __name__ == "__main__":
    main()
