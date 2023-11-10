#!/usr/bin/env python3


# Conditionals are statements in computer programming that check the truthiness or falsiness of 
# something and perform different actions based on that result. 
# if, elif, else, and while are all conditional keywords in Python.


# Here is an example of using the if/else block.
var1 = True
# Test if a condition is true.
if var1 == True: 
    # If the condition is true, this indented block will execute.
    print('var1 is truthy!')
else:
    # If the condition is false, this indented block will execute.
    print('var1 is falsey!')


# The example above isn't very "Pythonic". We can make it a bit cleaner by doing this. Notice the 
# subtle difference. 
var1 = True
if var1:
    print('var1 is truthy!')
else:
    print('var1 is falsey!')


# Now let's check some math.
var1 = 1
var2 = 2
if var1 + var2 == 3:
    print('they add up to 3')
else:
    print('they dont add up to 3')


# Let's try using the elif. elif is a keyword that is a combination of 'else' and 'if'. It 
username = 'aaron'
if username == 'ben':
    print('the user ben has logged in')
# If we get here that means the username was NOT 'ben'. This line will test if the username is 'aaron'.
elif username == 'aaron':
    print('the user aaron has logged in')
# If the username was neither 'ben' nor 'aaron', enter the block below.
else:
    print('an unknown user has logged in')
