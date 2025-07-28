# Using SQLite with Python

## Example: Basic Operations

Create a file named `sql_test.py` and add the following code:

```python
import sqlite3

# Open a connection to the database
conn = sqlite3.connect('test.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')
conn.commit()

# Insert a record
cursor.execute(
    'INSERT INTO students (first_name, email) VALUES (?, ?)',
    ('John', 'foo@email.com')
)
conn.commit()

# Query all records
cursor.execute('SELECT * FROM students')

# Iterate through results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
```
