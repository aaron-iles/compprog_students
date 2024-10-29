# First, create a database.
cd /proj
sqlite3 example.db


# Now you are in a SQL shell.  Here are some common commands.
# --This will print out the schema of the entire database.
.schema

# --Get help.
.help

# --List all tables in the database.
.tables

# --This will exit the shell.
.exit


# Let’s set up your sqliterc file. Open the file ~/.sqliterc using a text editor and type the following into it. Save and close the file.
.headers ON
.mode line


#Follow this example to learn some of the basic functions. The commands below must be run after you have entered the SQL shell. See the first command up above to enter the shell.
# --This will create a new table in the database. With columns named "student_id", "first_name", and "email".
CREATE TABLE students (student_id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);

# --Add a student to the table.
INSERT INTO students (first_name, email) VALUES ("Aaron", "example@gmail.com");

# --Get all students in the table.
SELECT * FROM students;

# --Get a student from the table whose name is "Aaron".
SELECT * FROM students WHERE first_name='Aaron';

# --Delete a record from a table.
DELETE FROM students WHERE first_name='Aaron';

# --Delete an entire table.
DROP TABLE students;
