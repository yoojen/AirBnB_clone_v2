#!/usr/bin/python3
"""
build route by using flask
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb_home():
    """
    returns the homepage of hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    returns the hbnb location of the web
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
