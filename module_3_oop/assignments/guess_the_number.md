# Guess the Number

## Description
In this project, you will build a Python module that plays the game **"Guess the Number"** as an automated **guesser**. Your module should use intelligent logic to guess a secret number by receiving feedback after each guess.

The game rules and structure are similar to a binary search. You’ll design a flexible, class-based module that allows for easy testing and extension.

## Game Rules
1. The **secret holder** (a person or a separate program) thinks of an integer.
2. The **guesser** (your code) makes a guess.
3. The secret holder responds with one of:
    - `"higher"` – the guess was too low
    - `"lower"` – the guess was too high
    - `"correct"` – the guess was exactly right
4. The guesser continues making guesses until the response is `"correct"`.

## Requirements
- You must use at least one **class** to encapsulate guessing logic.
- Use a constructor (`__init__`) to initialize attributes such as:
  - Low and high bounds of the search range
  - The current guess
  - A guess counter or history if you choose
- Implement a method called `make_guess()` to return an integer guess.
- Implement a method `process_feedback(feedback: str)` to update the range based on the response.
- Include a method or loop to automatically continue guessing until `"correct"` is returned.
- Include proper **type hints** and **docstrings** for all functions and methods.
- Your code should follow **PEP 8** and **PEP 20** guidelines.
- Include a `main()` function guarded by `if __name__ == '__main__':`.
- You may simulate the secret holder in your code for testing or build a manual interface.

## Submission Checklist
- [ ] File `guess_the_number.py` created.
- [ ] Guesser class with `__init__`, `make_guess()`, and `process_feedback()` implemented.
- [ ] Complete game loop implemented.
- [ ] Code runs correctly and guesses the number efficiently.
- [ ] Code includes full docstrings and type hints.
- [ ] Code follows PEP 8 and PEP 20 guidelines.
- [ ] File pushed to GitHub and URL submitted.

## Grading Criteria
| Criteria                                   | Points |
|--------------------------------------------|--------|
| Class-based design and constructor          | 4 pts  |
| Guessing logic implemented effectively      | 4 pts  |
| Feedback handling updates range correctly   | 3 pts  |
| Full game loop runs and terminates correctly| 2 pts  |
| Clean, readable code with docs & typing     | 2 pts  |

**Total**: 15 points

## Resources
- [PEP 8 – Style Guide](https://peps.python.org/pep-0008/)
- [PEP 20 – Zen of Python](https://peps.python.org/pep-0020/)
- [Python Classes](https://docs.python.org/3/tutorial/classes.html)
