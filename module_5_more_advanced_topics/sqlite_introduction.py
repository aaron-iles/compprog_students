#!/usr/bin/env python3


# To use SQLite with Python, create a new file called “sql_test.py” in /proj and write the following to it.
import sqlite3

# Open a connection to the database
conn = sqlite3.connect('test.db')

# Create a cursor
cursor = conn.cursor()

# Create a table.
cursor.execute('CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)')
conn.commit()

# Insert a new record
cursor.execute('INSERT INTO students (first_name, email) VALUES (?, ?)', ('John', 'foo@email.com'))
conn.commit()
# Get all of the records from the students table.
cursor.execute('SELECT * FROM students')

# Iterate through the results.
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
