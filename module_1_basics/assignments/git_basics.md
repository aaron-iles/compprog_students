# Git Basics

## Description
Git is the most popular version control system on earth. Every developer must learn the basics of git if they wish to contribute to a team. This exercise is meant to get you comfortable with some basic git commands. In module 0 we created a GitHub account, created a repository, and cloned the student repo and your own repo already.
Here is a cheat sheet for future reference: [git cheat sheet](../resources/git_cheat_sheet.sh)

## Instructions
### Run the commands
```bash

# Enter your git repo
cd ~/proj/compprog_class

# Configure your username and email
git config --global user.name "fist name last name"
git config --global user.email "your email"

# Open a file in this current directory with Sublime and write something in it
subl test.txt

# Now stage the file
git add test.txt

# Commit the file 
git commit -m "adding a test file for my class assignment"

# Push the commit
git push
```
### Submit the assignment
To indicate completion and prove the directions were followed, please submit a link to the file you pushed in your git repo. You can find this URL by following these steps
1. Log into GitHub.
2. Open your repository (remember it is called "compprog_class").
3. Find the file you pushed up ("test.txt") and click on it.
4. Copy the URL in the address bar and submit that with this assignment for credit.
