# Bash Basics

## Description
This exercise is meant to get you comfortable with Bash commands and using the terminal to control your computer via the command-line interface (CLI). You'll walk through and perform each command step-by-step.

## Instructions

1. Open your virtual machine (VM).
2. Open the **Terminal** application (search for it in the applications menu).
3. Type each of the following commands **in order**, observing what each one does:

    ```bash
    # Change directory to /tmp
    cd /tmp

    # Make a directory called sandbox
    mkdir sandbox

    # Change into the sandbox directory
    cd sandbox

    # List the contents (should be empty)
    ls

    # Go back one directory
    cd ..

    # Print working directory
    pwd

    # Remove the empty sandbox directory
    rmdir sandbox

    # Make a new directory
    mkdir sandbox2

    # Change into sandbox2
    cd sandbox2

    # Create a blank file
    touch test_file.txt

    # List directory contents
    ls

    # Open the file with Sublime. Type "hello world", save, and close the editor
    subl test_file.txt

    # Display the contents of the file
    cat test_file.txt

    # Try tab-completion: type "cat tes" and press Tab twice. Did it complete to "test_file.txt"?

    # Go back one directory
    cd ..

    # Try to remove the directory (will fail if not empty)
    rmdir sandbox2

    # Move the file out of sandbox2 to current directory
    mv sandbox2/test_file.txt .

    # Show contents of current directory (should now include test_file.txt)
    ls

    # Remove the sandbox2 directory recursively and forcefully
    rm -rf sandbox2

    # Rename the file
    mv test_file.txt new_file.txt

    # Delete the file
    rm new_file.txt
    ```

## Examples & Test Cases

| Command                 | Expected Output              |
|------------------------|------------------------------|
| `pwd`                  | `/tmp` (or similar path)     |
| `ls` (inside sandbox)  | *(no output, it's empty)*    |
| `cat test_file.txt`    | `hello world`                |
| `ls` (after `mv`)      | `test_file.txt` appears      |

## Submission Checklist
- [ ] All commands were executed in order.
- [ ] Output from key commands (`pwd`, `ls`, `cat`) was observed and understood.
- [ ] `test_file.txt` was successfully created, edited, moved, renamed, and deleted.
- [ ] You practiced tab completion at least once.

## Grading Criteria

| Criteria                            | Points |
|-------------------------------------|--------|
| Completed all Bash operations       | 10 pts |
| Demonstrated use of tab completion  | 2 pts  |
| Understood and explained each step  | 3 pts  |

**Total**: 15 points

## Resources
- [Bash Cheat Sheet](../resources/bash_cheat_sheet.sh)
