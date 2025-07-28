# SQLite CLI Usage

## Creating a Database
To start working with SQLite from the command line:

```bash
cd /proj
sqlite3 example.db
```

This launches the SQLite shell and creates a file named `example.db`.

## Common SQLite Shell Commands

```sql
-- Print out the schema of the entire database
.schema

-- Get help
.help

-- List all tables in the database
.tables

-- Exit the shell
.exit
```

## Configure Your SQLite Shell

Edit the file `~/.sqliterc` and add the following:

```text
.headers ON
.mode line
```

This configures the shell to display headers and output in a readable format.

## Basic Example in the SQL Shell

After launching `sqlite3 example.db`, run the following commands:

```sql
-- Create a new table
CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- Insert a record
INSERT INTO students (first_name, email) VALUES ("Aaron", "example@gmail.com");

-- Query all students
SELECT * FROM students;

-- Query a specific student
SELECT * FROM students WHERE first_name='Aaron';

-- Delete a specific record
DELETE FROM students WHERE first_name='Aaron';

-- Delete the table
DROP TABLE students;
```
