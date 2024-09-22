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


# Here is an example using multiple conditions. Note how using the 'and' keyword makes the
# conditional more strict.
movie_showtime = 'night'
attendee_age = 15
if movie_showtime == 'night' and attendee_age >= 18:
    print('the ticket is $20')
elif movie_showtime == 'night' and attendee_age < 18:
    print('the ticket is $15')
elif movie_showtime == 'day' and attendee_age >= 18:
    print('the ticket is $15')
elif movie_showtime == 'day' and attendee_age < 18:
    print('the ticket is $10')


# Let's take that same example above and use nested conditionals to make the logic cleaner.
movie_showtime = 'night'
attendee_age = 15
if movie_showtime == 'night':
    if attendee_age >= 18:
        print('the ticket is $20')
    else:
        print('the ticket is $15')
elif movie_showtime == 'day':
    if attendee_age >= 18:
        print('the ticket is $15')
    else:
        print('the ticket is $10')


# Here is an example using multiple conditions with the 'or' operator.
class_grade = 'A'
if class_grade == 'A' or class_grade == 'B':
    print('wow youre doing great!')
elif class_grade == 'C':
    print('youre doing aight my friend')
elif class_grade == 'D' or class_grade == 'F':
    print('mmm not good...')
else:
    print('grade not recognized')
