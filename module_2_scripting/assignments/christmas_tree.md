# Oh Christmas Tree!

## Description
This exercise is to write a Python program that prints a Christmas tree to the terminal. The height of the tree should be specified as a command-line argument.

## Instructions

1. Create a Python file named `tree_builder.py`.
2. The script should accept one argument: the desired height of the tree.
3. The script should validate the input:
   - Must be a **positive integer**
   - Height must be within **reasonable bounds** (e.g., not too large or negative)
4. If the input is valid, print a tree of the specified height using ASCII characters.
5. If the input is invalid or missing, print a helpful error or usage message.
6. Push the script to your GitHub repo and submit the URL of the file.

## Examples & Test Cases

| Command                         | Expected Output                                |
|--------------------------------|------------------------------------------------|
| `./tree_builder.py 10`         | Prints a tree 10 lines tall                    |
| `./tree_builder.py 0`          | Error: height must be >= 1                     |
| `./tree_builder.py -10`        | Error: height must be >= 1                     |
| `./tree_builder.py 5.8`        | Error: height must be a positive integer       |
| `./tree_builder.py abc`        | Error: height must be a positive integer       |
| `./tree_builder.py`            | Prints a help/usage message                    |
| `./tree_builder.py 10000000`   | Error: height exceeds maximum allowed          |

## Submission Checklist
- [ ] Script named `tree_builder.py`.
- [ ] Accepts and validates command-line argument for height.
- [ ] Prints a tree of specified height if input is valid.
- [ ] Gracefully handles invalid or missing input.
- [ ] File pushed to GitHub and URL submitted.

## Grading Criteria

| Criteria                                      | Points |
|-----------------------------------------------|--------|
| Valid input creates a correct tree             | 8 pts  |
| Input validation and helpful error messages    | 5 pts  |
| Program handles edge cases and invalid input   | 2 pts  |

**Total**: 15 points

## Resources
- [Python sys.argv Reference](https://docs.python.org/3/library/sys.html)
- [Input Validation Techniques](https://realpython.com/python-exceptions/)
