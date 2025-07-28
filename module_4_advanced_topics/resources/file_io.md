# Python File I/O – Resource Guide

## Overview
This guide introduces the basics of reading and writing files in Python using built-in tools. Python provides a simple interface to handle files through the `open()` function, most effectively used with a **context manager** (`with` statement).

---

## Writing to a File

To write to a file, open it in **write mode** (`'w'`). If the file doesn't exist, it will be created. If it already exists, its contents will be **overwritten**.

```python
with open('/tmp/example.txt', 'w') as f:
    f.write('hello world!')
```

---

## Reading from a File

To read from a file, open it in **read mode** (`'r'`). The file must exist, or Python will raise a `FileNotFoundError`.

```python
with open('/tmp/example.txt', 'r') as f:
    text = f.read()

print(text)
```

---

## Handling Missing Files

Trying to open a non-existent file in read mode will raise an error:

```python
with open('/tmp/foo.txt', 'r') as f:
    # This will raise FileNotFoundError if '/tmp/foo.txt' does not exist
```

To handle this gracefully, use `try`/`except`:

```python
try:
    with open('/tmp/foo.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found!")
```

---

## Only Strings or Bytes Can Be Written

You can only write **strings** or **bytes** to a file. If you're working with other data types (like dictionaries), convert them to a string first (e.g., using `str()` or `json.dumps()`):

```python
some_dict = {"foo": "bar"}

with open('/tmp/example.txt', 'w') as f:
    f.write(str(some_dict))  # OK but not great for structured data
```

For structured data, consider using the `json` module:

```python
import json

with open('/tmp/example.json', 'w') as f:
    json.dump(some_dict, f)
```

---

## File Modes Reference

| Mode | Description                    |
|------|--------------------------------|
| `'r'` | Read (default)                 |
| `'w'` | Write (overwrite)              |
| `'a'` | Append                         |
| `'b'` | Binary                         |
| `'+'` | Read and write                 |

---

## Best Practices

- Always use a **context manager** (`with`) to ensure files are closed properly.
- Use the `json` module when writing and reading structured data like dictionaries.
- Handle `FileNotFoundError` when reading files that may not exist.

---

## More Resources

- [Python Built-in `open()` Documentation](https://docs.python.org/3/library/functions.html#open)
- [Python `json` Module](https://docs.python.org/3/library/json.html)
