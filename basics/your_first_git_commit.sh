# Install git
sudo dnf install git -y

# Change directories into your projects directory
cd /proj/

# Clone your own git repo
git clone git@github.com:<your GitHub username>/compprog_class.git

# Enter your git repo directory
cd /proj/compprog_class/

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



# That's it! Now here is some more information...

# If you made changes to your git repo elsewhere and needed to pull them down to your VM
cd /proj/compprog_class/
git pull

# Now say you made changes to a file that you wanted to undo
git checkout -- some_file_i_wanted_to_undo.txt
