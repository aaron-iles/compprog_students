# Simple API Server

## Description
In this assignment, you'll build a basic REST API using Flask and SQLite. You'll implement three endpoints that interact with a `users` table in a SQLite database. The provided starter code includes the API skeleton—you will fill in the missing logic to make it functional.

This assignment will help you demonstrate your understanding of:
- Flask and Flask-RESTx
- RESTful endpoints (`GET`, `POST`)
- Request handling
- Database querying and writing using `sqlite3`
- API routing and argument parsing

## Instructions
1. Create a file in your GitHub repo called `simple_api.py`.
2. Copy and paste the provided starter code below into your file.
3. Complete the `TODO` sections to implement the logic for:
   - Returning all users from the database (`GET /users`)
   - Adding a new user (`POST /users`)
   - Returning a user by ID (`GET /users/<int:user_id>`)
4. Add, commit, and push the file to GitHub.
5. Submit the URL of your `simple_api.py` file.

```python
#!/usr/bin/env python3

import sqlite3
import argparse
from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="This is a simple API for interacting with a database.",
    )
    p.add_argument(
        "-d", "--database", required=True, type=str, dest="database_path",
        help="The path to the database to which to connect."
    )
    return p.parse_args()

def init_database(path: str) -> None:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)"
    )
    conn.commit()

@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"message": "hello"}

@api.route("/users")
class UsersAPI(Resource):
    def get(self):
        # TODO: Get all users from the database and return them.
        return

    def post(self):
        data = request.get_json()
        # TODO: Insert data (name, email) into the database.
        return

@api.route("/users/<int:user_id>")
class UserAPI(Resource):
    def get(self, user_id: int):
        # TODO: Return user with given ID, formatted as: {"name": ..., "email": ...}
        return

if __name__ == "__main__":
    args = parse_args()
    database = args.database_path
    init_database(database)
    app.run(host="127.0.0.1", port=8080, debug=True, threaded=False)
```

## Examples & Test Cases

| Endpoint                | Method | Example Command                                        |
|-------------------------|--------|--------------------------------------------------------|
| `/ping`                 | GET    | `curl http://127.0.0.1:8080/ping`                     |
| `/users`                | GET    | `curl http://127.0.0.1:8080/users`                    |
| `/users`                | POST   | `curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com"}' http://127.0.0.1:8080/users` |
| `/users/<user_id>`      | GET    | `curl http://127.0.0.1:8080/users/1`                  |

## Submission Checklist
- [ ] File named `simple_api.py` created
- [ ] Logic completed for all endpoints
- [ ] File pushed to GitHub
- [ ] URL submitted

## Grading Criteria

| Criteria                             | Points |
|--------------------------------------|--------|
| `GET /users` implemented correctly   | 3 pts  |
| `POST /users` implemented correctly  | 3 pts  |
| `GET /users/<id>` implemented        | 3 pts  |
| Code readability and formatting      | 1 pt   |

**Total**: 10 points

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [sqlite3 module](https://docs.python.org/3/library/sqlite3.html)
