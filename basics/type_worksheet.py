#!/usr/bin/env python3


# INSTRUCTIONS #
# 1. Copy this file into your own Git repo.
# 2. Fill out lines 12 - 22 in order to make this file execute properly.
# 3. Add, commit, and push the file to your repo.


# TODO
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


try:
    assert type(a) == int
except AssertionError:
    print(f"{a} is not an integer! it is a {type(a)}")
else:
    print(f"Correct! {a} is an integer")


try:
    assert type(b) == float
except AssertionError:
    print(f"{b} is not a float! it is a {type(b)}")
else:
    print(f"Correct! {b} is a float")


try:
    assert type(c) == type_c
except AssertionError:
    print(f"{c} is not a {type_c}! it is a {type(c)}")
else:
    print(f"Correct! {c} is a {type(c)}")


try:
    assert type(d) == str
except AssertionError:
    print(f"{d} is not a string! it is a {type(d)}")
else:
    print("Correct! {d} is a string")


try:
    assert type(e) == bool
except AssertionError:
    print(f"{e} is not a boolean! it is a {type(e)}")
else:
    print("Correct! {e} is a boolean")
