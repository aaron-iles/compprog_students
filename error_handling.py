#!/usr/bin/env python3


def subtract(a: int, b: int) -> int:
    try:
        return a - b
    except TypeError:
        print("you input the wrong type!")
        return


def add(a: int, b: int) -> int:
    return a + b


def nth_item(input_list: list, index: int):
    return input_list[index]


def eval_expression(expression: str) -> None:
    eval(expression)
    return


# Don't edit these!
def main():
    subtract("world", 19)
    add(1, "hello")
    nth_item([1, 2, 3, 4], 16)
    eval_expression("print(my_var)")
    return


if __name__ == "__main__":
    main()
