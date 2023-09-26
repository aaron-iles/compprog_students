# Install git
sudo dnf install git -y

# Stage a file
git add <filename>

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
