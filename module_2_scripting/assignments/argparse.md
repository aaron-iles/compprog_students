# Argument Parsing

## Description
Write a Python script named `convert.py` that performs basic unit conversions using command-line arguments. The script should support the following types of conversions:

- Kilometers to miles
- Celsius to Fahrenheit
- Kilograms to pounds

## Instructions

1. Create a Python file in your Git repository named `convert.py`.
2. Use the `argparse` module to parse two command-line arguments:
   - `--type`: the type of conversion (`km_to_miles`, `c_to_f`, or `kg_to_lb`)
   - `--value`: the numerical value to convert (float)
3. Based on the `--type` argument, perform the correct conversion:
   - `km_to_miles`: multiply by 0.621371
   - `c_to_f`: use the formula `(value * 9/5) + 32`
   - `kg_to_lb`: multiply by 2.20462
4. Print the result with appropriate units, rounded to two decimal places.
5. Test the script using the examples below.
6. Add, commit, and push the script to your GitHub repository.
7. Submit the GitHub URL of your `convert.py` file.

## Examples & Test Cases

| Command                                     | Expected Output                          |
|--------------------------------------------|------------------------------------------|
| `./convert.py --type km_to_miles --value 5` | `5.0 kilometers is 3.11 miles`           |
| `./convert.py --type c_to_f --value 100`    | `100.0°C is 212.0°F`                     |
| `python3 convert.py --type kg_to_lb --value 70` | `70.0 kilograms is 154.32 pounds`   |

## Submission Checklist
- [ ] Script is named `convert.py`.
- [ ] Script uses `argparse` to parse `--type` and `--value`.
- [ ] Script supports all 3 conversions correctly.
- [ ] Script prints well-formatted, rounded output.
- [ ] File added, committed, and pushed to GitHub.
- [ ] Submitted the correct URL to your file in GitHub.

## Grading Criteria

| Criteria                                       | Points |
|------------------------------------------------|--------|
| Parses and handles arguments correctly         | 5 pts  |
| Performs all 3 conversions correctly           | 6 pts  |
| Output formatting and readability              | 2 pts  |
| Proper naming and submission                   | 2 pts  |

**Total**: 15 points

## Resources
- [Python argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [argparse example](../resources/argparse_example.py)
