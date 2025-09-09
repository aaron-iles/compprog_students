# GitHub Setup

## Description
In this assignment we will create a GitHub account and do some configuration. GitHub is cloud-based repository for maintaining software. As a developer, learning and understanding how to use git is a critical skill. There are many different ways to host a git repo, but GitHub is one of the most popular and robust platforms. 
See [this link](https://github.com/about) to learn more about GitHub.

## Instructions
### Create a GitHub account
1. On [this page](https://github.com/) click "Sign up for GitHub".
2. Enter your PERSONAL email (if you have one). You will want to keep this account forever.
3. Follow the rest of the prompts for setting up your account. 

### Add an SSH key
Follow [these instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=webui) for adding an ssh key. This enables you to interact with GitHub from the command line.

### Create class repository
1. Log into GitHub.
2. Click "Repositories" in the top left. This will show you all of the repos in your GitHub account.
3. Click "New" in the top right.
4. Name your repository "compprog_class".
5. Set your repo to "Private".
6. Click "Create Repository".
7. Share the repository with me by clicking "Invite collaborators" > "Add people" > type "aaron-iles".

### Clone the student materials repo
Let's clone the student repo. Later on we will talk more about git. In your VM, run the following commands using the "terminal" application:
```bash
# Only do this AFTER you have created your GitHub account and added an ssh key.

# Create and enter your projects directory.
cd ~
mkdir proj
cd proj

# Install git
sudo dnf install git -y

# Now clone the student material repository.
git clone git@github.com:aaron-iles/compprog_students.git

# Open up the repo and take a look.
cd compprog_students
ls -la

# Check which branch you are on.
git status
git branch
```

### Clone your git repo
Now let's clone the repo we made in GitHub.
```bash
cd ~/proj

# Replace [your username] with your git username. Look at the URL in your address bar to determine what this is.
git clone git@github.com:[your username]/compprog_class.git

cd compprog_class
git status
```

### Update your bash profile
Last step! There are a number of scripts that run when you log in that change how your environment behaves. We are going to inject some commands to make it a bit better by using a file called `.bash_profile`. 
1. Copy the file [.bash_profile](../resources/.bash_profile) into your home directory in your VM. ==NOTE:== the file must be named `.bash_profile` not `bash_profile`! You can also find this file inside the compprog_students git repository that you just cloned up above.
2. Log out of your VM.
3. Log back into your VM, open a terminal, and run the following command:
```
testme
```
4. Did you see a message get printed to the screen saying "it worked!"?
