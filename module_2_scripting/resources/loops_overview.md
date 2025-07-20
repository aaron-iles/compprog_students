# Loops

## `for` Loops
Here is an example of a basic `for` loop. Note how a variable "number" is declared and that variable takes on the value of the item in the list over which we are iterating.
```python
for number in [1, 2, 3]:
    print(number)
```

For loops must be run on "iterables". These include lists, tuples, dicts, strings, and more!
```python
for letter in "abcdefg":
    print(letter)
```

You can use loops to sum lists. This isn't the best way to do it, but it can be done.
```python
total = 0
for i in [3, 6, 8, 1, 100]:
    # The below syntax is the same as saying
    # total = total + i
    total += i
print(total)
```

You can use for loops to print some nice ASCII art.
```python
for i in range(5):
    print('')
    for j in range(8):
        print('#', end='')
```

## `while` Loops
The while loop is a mix between a conditional and a loop. It loops so long as a condition is true. Note that a while statement must be evaluated against a boolean.
```python
total = 0
while total < 10:
    total += 1
    print(f'the current total is {total}')
```

This loop will run forever.
```python
while True:
    print('I will never stop')
```
