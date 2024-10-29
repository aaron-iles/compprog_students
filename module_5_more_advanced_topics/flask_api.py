#!/usr/bin/env python3


import sqlite3
import argparse
import sys
from flask import Flask, make_response
from flask import request
from flask_restx import Resource, Api

# Create globals for your application and API objects.
app = Flask(__name__)
api = Api(app)


def parse_args() -> argparse.Namespace:
    """
    Parses the arguments from the command line.

    :return argparse.Namespace: The namespace of the arguments that were parsed.
    """
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="This is a simple API for interacting with a database.",
    )
    p.add_argument(
        "-d",
        "--database",
        required=True,
        type=str,
        dest="database_path",
        help="The path to the database to which to connect.",
    )
    return p.parse_args()


def init_database(path: str) -> None:
    """
    Creates a database at the given path and instantiates the table.

    :param str path: The path to the database file to be created.
    :return None:
    """
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE)"
    )
    conn.commit()
    return


@api.route("/ping")
class Ping(Resource):
    """
    This resource holds the endpoints for checking the health of the API.
    """

    def get(self):
        """
        Check the API health by returning a simple hello.
        """
        return {"message": "hello"}


@api.route("/users")
class UsersAPI(Resource):
    """
    This resource holds the endpoints for interacting with users
    """

    def get(self):
        """
        Gets all users in the database.
        """
        print('in here!')
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def post(self):
        """
        """
        # TODO: How do you get the data from a POST? Maybe use request.form?
        return make_response({"message": "user added successfully"}, 201)


@api.route("/users/<int:user_id>")
class UserAPI(Resource):
    """
    """
    def get(self, user_id: int):
        # TODO
        # This is asking for a specific user by ID. Your job is to return the user name and email.
        # ie: {"name": "foo", "email": "foo@gmail.com"}
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=(?)", (user_id,))
        results = cursor.fetchall()
        print(results)
        # TODO put the results into the response
        return make_response({}, 200)




if __name__ == "__main__":
    args = parse_args()
    database = args.database_path
    init_database(database)
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=False)
