# Git Basics

## Description
Git is the most popular version control system on earth. Every developer must learn the basics of Git if they wish to contribute to a team. This exercise is meant to get you comfortable with some basic Git commands. In Module 0, you created a GitHub account, created a repository, and cloned both the student repo and your own repo.

## Instructions

1. Enter your cloned repository:
    ```bash
    cd ~/proj/compprog_class
    ```

2. Configure your Git username and email (use your actual name and email):
    ```bash
    git config --global user.name "first name last name"
    git config --global user.email "your email"
    ```

3. Open a file in Sublime and write something in it:
    ```bash
    subl test.txt
    ```

4. Stage the file:
    ```bash
    git add test.txt
    ```

5. Commit the file:
    ```bash
    git commit -m "adding a test file for my class assignment"
    ```

6. Push the commit:
    ```bash
    git push
    ```

### Submit the Assignment

To indicate completion and prove the directions were followed, submit a **link to the file** you pushed in your GitHub repo. You can find this link by:

1. Logging into [GitHub](https://github.com).
2. Opening your `compprog_class` repository.
3. Clicking on the `test.txt` file you pushed.
4. Copying the URL from the address bar and submitting that.

## Examples & Test Cases

| Command               | Expected Output                          |
|----------------------|------------------------------------------|
| `git add test.txt`   | *(no output if successful)*              |
| `git commit -m ...`  | `1 file changed, 1 insertion(+)`         |
| `git push`           | Pushes the commit to GitHub successfully |

## Submission Checklist
- [ ] Git username and email configured.
- [ ] File `test.txt` created and edited.
- [ ] File staged, committed, and pushed to GitHub.
- [ ] Link to the pushed file submitted.


## Resources
- [Git Cheat Sheet](../resources/git_cheat_sheet.sh)
