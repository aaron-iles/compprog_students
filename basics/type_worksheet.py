#!/usr/bin/env python3


# INSTRUCTIONS #
# 1. Copy this file into your own Git repo.
# 2. Fill out lines 12 - 28 in order to make this file execute properly.
# 3. Execute this file by running python3 type_worksheet.py.
# 4. Make sure you got all "Correct!" messages and no "Oops!" messages.
# 5. Add, commit, and push the file to your repo.


# TODO START
# Store any integer in the var "a".
a = 
# Store any float in the var "b".
b = 
# Add a and b and store it in "c" so that c is the sum of a and b.
c = 
# Now state what the type of the var c is. (Hint: it will be float, int, str, bool, etc.)
type_c = 
# Store any string in the var "d".
d = 
# Store any boolean in the var "e".
e = 
# Make a list and store it in "f".
f = 
# Make a set and store it in "g".
g = 
# Make a dictionary and store it in "h".
h = 
# TODO END


# NOTE: Don't edit any of this.
def check_answer(var, var_type):
    try:
        assert type(var) == var_type
    except AssertionError:
        print(f"Oops! {var} is not a {var_type} it is a {type(var)}")
    else:
        print(f"Correct! {var} is a {var_type}")
    return


check_answer(a, int)
check_answer(b, float)
check_answer(c, type_c)
check_answer(d, str)
check_answer(e, bool)
check_answer(f, list)
check_answer(g, set)
check_answer(h, dict)
