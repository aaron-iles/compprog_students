# Install git
sudo dnf install git -y

# NOTE: All git commands must be run from inside a git repository!

# Stage a file
git add my_file.txt

# Commit a file 
git commit -m "here is my commit message"

# Stage and commit all files
git commit -a -m "here is my commit message"

# Push the commit
git push

# Pull the latest changes
git pull

# Undo the changes to a file locally
git checkout -- <filename>

# Undo changes to all files locally
git checkout -- .
