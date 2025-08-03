#!/usr/bin/env python3

import argparse
import json
import logging
import sys
import eventlet
import socketio

from flask import Flask, render_template, request



def setup_logging(verbose: bool = False):
    """
    Configures the logging module to output log messages to stdout. This function sets up a stream
    handler to log messages to stdout with the specified logging format. It adds the stream handler
    to the root logger and sets the logging level.

    :param bool verbose: True if the application should be run verbosely and False otherwise.
    :return None:
    """
    # Define the logging format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    # Create a stream handler to log to stdout since the application will log via journald.
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(log_format))
    # Add the stream handler to the root logger
    logging.root.addHandler(stream_handler)
    # Set the logging level.
    logging.root.setLevel(logging.DEBUG if verbose else logging.INFO)


def parse_args() -> argparse.Namespace:
    """
    Parses the arguments from the command line.

    :return argparse.Namespace: The namespace of the arguments that were parsed.
    """
    p = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="This is a description of my module.",
    )
    p.add_argument("-v", required=False, action="store_true", dest="verbose", help="Run verbosely.")
    return p.parse_args()


@app.route("/", methods=["GET"])
def get_basic():
    """
    Fill this out.

    :return tuple: The rendered HTML page.
    """
    return render_template("my_page.html")


# Read in the config file.
def start_application():
    args = parse_args()
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    app = flask.Flask(__name__)
    socketio = SocketIO(app)
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)
    return
