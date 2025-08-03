# Using Black for Code Formatting

`black` is a command-line utility written in Python that will aggressively reformat your code **in place** to comply with [PEP 8](https://peps.python.org/pep-0008/). It is a valuable tool for maintaining consistent and readable code formatting across your projects.

## Installation

To install `black`, run the following command:

```
python3 -m pip install black --user
```

## Basic Usage

To run `black` on a single file named `my_file.py`, use:

```
black --line-length 100 my_file.py
```

## Formatting Multiple Files

You can run `black` on all Python files in a directory using a wildcard:

```
black --line-length 100 *.py
```

This will apply the formatting rules to each `.py` file in the current directory.

## Additional Resources

- [Black Documentation](https://black.readthedocs.io/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
