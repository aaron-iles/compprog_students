# Colored Output

To print colored output you will need to use ANSII escape codes. See the colors section here: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

```python
print("\033[32mhere is some green text\033[0m")
print("\033[32;1mhere is some bold green text\033[0m")
print("\033[31mhere is some red text\033[0m")
print("\033[31;44mhere is some red text on a blue backgroup\033[0m")

# Here is the whole table.
for fg_color in range(30, 38):
    for bg_color in range(40, 48):
        print(f"[{fg_color} {bg_color} \033[{fg_color};{bg_color}mabcABC123\033[0m] ", end='')
    print('')

def print_surprise():
    star_6 = f'\033[1;37;44m   ★\033[0m'
    star = f'\033[1;37;44m★\033[0m'
    blank_star = f'\033[1;37;44m \033[0m'
    star_5 = f'\033[1;37;44m ★  \033[0m'
    red = f'\033[1;31m█\033[0m'
    white = f'\033[1;37m█\033[0m'
    line_a = f'{star}{star_6 * 5}{blank_star}{red * 50}'
    line_b = f'{blank_star}{star_5 * 5}{blank_star}{white * 50}'
    print(f'{line_a}\n{line_b}\n' * 4, end='')
    print(line_a)
    print(f'{white * 72}\n{red * 72}\n' * 4)
    return
```
