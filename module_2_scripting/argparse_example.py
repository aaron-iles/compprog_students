#!/usr/bin/env python3


import argparse


def parse_args() -> argparse.Namespace:
    """
    Parses the arguments from the command line.

    :return argparse.Namespace: The namespace of the arguments that were parsed.
    """
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="This is a description of my module.",
    )
    p.add_argument(
        "-t",
        required=True,
        type=int,
        dest="tree_height",
        help="The height of the tree (in characters). This must be a positive integer.",
    )
    p.add_argument(
        "-a",
        required=False,
        type=bool,
        dest="always_delete",
        default=False,
        help="True if this module should always delete the working directory and False otherwise.",
    )
    p.add_argument(
        "-o",
        "--operation",
        required=True,
        type=str,
        dest="operation",
        choices=["add", "multiple", "divide"],
        help="Tasdasdasdasd"
    )

    return p.parse_args()


def main():
    args = parse_args()
    if args.operation == 'add':
        result = add(args.number_a, args.number_b)
    elif ...:
        ...
    print(result)
    return


if __name__ == "__main__":
    main()
