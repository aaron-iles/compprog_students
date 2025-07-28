# Storage Part 2: SQLite

## Description
In this exercise, you will demonstrate your ability to use SQLite both through the **command line** and in **Python**. You will create a simple student database, perform common operations, and practice integrating SQLite in a Python script.

## Part 1: SQLite CLI

1. Create a new database:
    ```bash
    cd /proj
    sqlite3 school.db
    ```

2. Inside the SQLite shell:
    - Create a table called `students` with the following columns:
        - `student_id` (INTEGER, PRIMARY KEY)
        - `first_name` (TEXT, NOT NULL)
        - `email` (TEXT, NOT NULL, UNIQUE)
    - Insert at least 3 records.
    - Run a `SELECT` query to show all records.
    - Run a `DELETE` query to remove one record.
    - Exit the shell.

## Part 2: Python Integration

1. Create a new file called `school_db.py`.
2. Use the `sqlite3` module to:
    - Connect to the same `school.db` database.
    - Query all students.
    - Print out the list of students.

## Submission Checklist

- [ ] File `school.db` exists with correct table and records.
- [ ] `school_db.py` queries and prints students.
- [ ] You committed and pushed your work to GitHub.
- [ ] You submitted the GitHub URL for grading.

## Grading Criteria

| Task                             | Points |
|----------------------------------|--------|
| Created table and inserted data  | 5 pts  |
| Deleted record and queried data  | 3 pts  |
| Python script retrieves records  | 5 pts  |
| Clean code and clear output      | 2 pts  |

**Total**: 15 points

## Resources
### [SQLite CLI usage](../resources/sqlite_cli_usage.md)
### [SQLite python usage](../resources/sqlite_python_usage.md)
