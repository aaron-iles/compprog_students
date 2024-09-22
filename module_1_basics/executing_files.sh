# We won’t be using IDEs for programming in this class. We will be using the true engineer’s method: 
# text files. Python scripts are just simple text files and they are executed using the system’s 
# Python interpreter. You can create a Python script from the command line or from the GUI. 
# Below is an example of how to create a Python script.

# Create an empty file by using the touch command.
cd /proj
touch my_script.py

# cat is a command that ‘concatenates’ files. You can use this to read a file. Run the cat command 
# on the file you just created to see that it is empty.
cat my_script.py

# The script is currently not executable. This is a control set on files in Unix that determines 
# file permissions. To make a script executable, use the chmod command like this:
chmod 770 my_script.py

# The script can be run by running the Python interpreter with the filename as the first argument.
python3 my_script.py

# Notice nothing happened since my_script.py is empty, but the Python interpreter DID run it!
# Let's try making our script do something. Open my_script.py in sublime
subl my_script.py

# Now type the following into the file and save it when you're done:
print("Hello World!")

# Now exit sublime and execute the file in your terminal just like you did before.
python3 my_script.py

# Did you see anything get written to the terminal? If so, carry on. If not, raise your hand.

# Another way to run a script is by setting the shebang at the top of the file. This is set on line 
# 1 of the file and starts with "#!" (hash-bang -> shebang). For python3 you will want to use the 
# shebang "#! /usr/bin/env python3". Don't worry about the details yet, just take my word for it.

# Below is a simple Python script. Write this into the file you created above called my_script.py.
# NOTE: The shebang (#! /usr/bin/env python3) needs to be the first line of the file!!

#! /usr/bin/env python3
print("Hello World!")


# Now execute the file using the following syntax. You should see "Hello World" printed to the 
# screen.
./my_script.py
