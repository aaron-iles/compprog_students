# To perform these operations, you will need to open your VM, open the "Terminal" application 
# (search for it in the applications menu), and type each of the following commands into the terminal. 

# Change dirs to /tmp
cd /tmp

# Make a dir called sandbox
mkdir sandbox

# Change dirs to sandbox
cd sandbox

#  List the contents of the dir (empty)
ls

# Go back one dir
cd ..

# Echo the present working dir
pwd

# Remove the sandbox dir (only works when empty)
rmdir sandbox

# Make another dir
mkdir sandbox2

# Change dirs to sandbox2
cd sandbox2

# Create a blank file
touch test_file.txt

# Show the contents of the directory
ls

# Open the file with sublime. Once it is open, type "hello world", save the file, and close Sublime
subl test_file.txt

# Read the contents of the file. Does it say "hello world"?
cat test_file.txt

# Start typing "cat tes" then hit the tab button twice. Did it autocomplete to "cat test_file.txt"?

# Go back one dir
cd ..

# Try to remove the dir (fails since it is not empty)
rmdir sandbox2

# Move the file out of the sandbox dir to the current dir (.)
mv sandbox2/test_file.txt .

# Show the contents of the current dir (do you see the test_file.txt?)
ls

# Now remove the dir forcefully and recursively
rm -rf sandbox2

# Rename the file from test_file.txt to new_file.txt
mv test_file.txt new_file.txt

# Delete the test file
rm new_file.txt
