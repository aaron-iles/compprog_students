#!/usr/bin/env python3

# To print colored output you will need to use ANSII escape codes. 
# See the colors section here: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors


print("\033[32mhere is some green text\033[0m")
print("\033[32;1mhere is some bold green text\033[0m")
print("\033[31mhere is some red text\033[0m")
print("\033[31;44mhere is some red text on a blue backgroup\033[0m")

# Here is the whole table.
for fg_color in range(30, 38):
    for bg_color in range(40, 48):
        print(f"[{fg_color} {bg_color} \033[{fg_color};{fg_color}mabcABC123\033[0m ", end='')
    print('')
