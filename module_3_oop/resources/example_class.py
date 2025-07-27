#!/usr/bin/env python3


class Example:
    """
    Here is the docstring for my example class.

    :param str arg1: The __init__ args are documented here.
    """

    def __init__(self, arg1: str):
        self.arg1 = arg1

    def method_1(self, arg1: str) -> None:
        """
        Here I document the method_1.

        :param str arg1: Docstring for arg1
        """
        return arg1


def main():
    my_object = Example("something")
    print(my_object.method_1("something else"))
    print(my_object.arg1)
    return


if __name__ == "__main__":
    main()
