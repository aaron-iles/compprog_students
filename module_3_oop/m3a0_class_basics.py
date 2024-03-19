#!/usr/bin/env python3


# INSTRUCTIONS
# For this assignment you will demonstrate the creation of a simple class. You may create a class to
# represent anything you would like: a person, vehicle, building, game... anything to which 
# attributes could be given and methods could be applied. The following MUST be demonstrated:
#    - The declaration of a class
#    - The declaration of the __init__ method
#    - The declaration of at least one method
#    - The declaration of at least one attribute
#    - The instantiation of the class
#    - A call to a method in the class
#    - A call to an attribute in the class
# Below you will find a module that does all of the above items. You must create your own class, 
# variables, methods, attributes, etc., but I provided this to help you get started. Remember PEP 8 
# and PEP 20. You must include docstrings and type hints.



class Example:
    """
    TODO
    """
    def __init__(self, arg1: str):
        self.arg1 = arg1

    def method_1(self, arg2: str) -> None:
        """
        TODO
        """
        # TODO
        return


def main():
    my_object = Example('something')
    print(my_object.method_1('something else')
    print(my_object.arg1)
    return


if __name__ == '__main__':
    main()
