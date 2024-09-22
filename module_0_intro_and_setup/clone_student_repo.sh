# Only do this AFTER you have created your GitHub account and added an ssh key.

# Create and enter your projects directory.
sudo mkdir /proj
sudo chown $USER:$USER /proj
sudo chmod 770 /proj
cd /proj

# Now clone the student material repository.
git clone git@github.com:aaron-iles/compprog_students.git

# Open up the repo and take a look.
cd compprog_students
ls -la
ls -la intro

# Check which branch you are on.
git status
git branch
