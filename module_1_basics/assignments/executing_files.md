# Executing Files

## Description
We won’t be using IDEs for programming in this class. We will be using the true engineer’s method: text files. Python scripts are just simple text files and they are executed using the system’s Python interpreter. You can create a Python script from the command line or from the GUI. Below is an example of how to create a Python script.

## Instructions
1. Create an empty file by using the touch command.
```bash
cd /tmp
touch my_script.py
```
2. `cat` is a command that ‘concatenates’ files. You can use this to read a file. Run the cat command on the file you just created to see that it is empty.
```bash
cat my_script.py
```
3. The script is currently not executable. This is a control set on files in Unix that determines file permissions. To make a script executable, use the `chmod` command like this:
```bash
chmod 770 my_script.py
```
4. The script can be run by running the Python interpreter with the filename as the first argument.
```bash
python3 my_script.py
```
5. Notice nothing happened since my_script.py is empty, but the Python interpreter DID run it! Let's try making our script do something. Open `my_script.py` in sublime
```bash
subl my_script.py
```
6. Now type the following into the file and save it when you're done:
```bash
print("Hello World!")
```
7. Now exit sublime and execute the file in your terminal just like you did before.
```bash
python3 my_script.py
```
8. Did you see anything get written to the terminal? If so, carry on. If not, raise your hand.
9. Another way to run a script is by setting the shebang at the top of the file. This is set on line 1 of the file and starts with "#!" (hash-bang -> shebang). For python3 you will want to use the shebang `#! /usr/bin/env python3`. Don't worry about the details yet, just take my word for it.
10. Below is a simple Python script. Write this into the file you created above called `my_script.py`. NOTE: The shebang (`#! /usr/bin/env python3`) needs to be the first line of the file!!
```python
#! /usr/bin/env python3
print("Hello World!")
```
11. Now execute the file using the following syntax. You should see "Hello World" printed to the screen.
```bash
./my_script.py
```
