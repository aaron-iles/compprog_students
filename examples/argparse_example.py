#!/usr/bin/env python3


import argparse


def parse_args() -> argparse.Namespace:
    """
    Parses the arguments from the command line.

    :return argparse.Namespace: The namespace of the arguments that were parsed.
    """
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="This is a description of my script.",
    )
    p.add_argument(
        "-t",
        required=True,
        type=int,
        dest="tree_height",
        help="The tree height must be a positive intege",
    )
    return p.parse_args()


def main():
    args = parse_args()
    print(type(args.tree_height))
    return


if __name__ == "__main__":
    main()
