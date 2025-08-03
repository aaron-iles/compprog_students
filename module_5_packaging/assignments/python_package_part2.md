# Python Package Project – Part 2

## Description
In this final part of your multi-week Python package project, you will complete and polish your package implementation. This includes writing unit tests, ensuring code quality and formatting, and building a distributable package (wheel). This exercise builds upon your work from Part 1.

## Instructions

1. Ensure all necessary files for your package are in the `package/` directory of your GitHub repository.
2. Add additional modules, classes, or functions to complete your package’s core functionality.
3. Write unit tests for your package using `pytest`.
4. Ensure your test coverage is **at least 50%**.
5. Apply code formatting using tools such as `black` or `flake8`.
6. Add or update the following configuration files in your package directory:
   - `pyproject.toml`
   - `setup.cfg`
   - `tox.ini`
7. Run `tox` to verify that:
   - All tests pass.
   - Your package builds successfully.
8. Build a wheel using:
   ```bash
   python3 -m pip install build
   python3 -m build
   ```
9. Commit and push all of your work to the `main` branch of your GitHub repository.
10. Submit the **link to your GitHub Pull Request (PR)** or repository.

## Submission Checklist
- [ ] All package files are in the `package/` directory.
- [ ] At least 50% test coverage is achieved.
- [ ] Code is formatted using a linter (e.g., black, flake8).
- [ ] `tox` runs successfully.
- [ ] Wheel can be built from the package.
- [ ] All code is committed and pushed to the `main` branch.
- [ ] GitHub PR or repo link is submitted.

## Grading Criteria

| Criteria                                 | Points |
|------------------------------------------|--------|
| Package functionality complete           | 10 pts |
| Code style and formatting                | 5 pts  |
| Test coverage ≥ 50%                      | 5 pts  |
| Successful `tox` and wheel build         | 5 pts  |
| Organized directory and documentation    | 5 pts  |

**Total**: 30 points

## Resources
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Tox Documentation](https://tox.readthedocs.io/en/latest/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Python Packaging Guide](https://packaging.python.org/)
