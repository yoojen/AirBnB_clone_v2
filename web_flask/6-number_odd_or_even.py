#!/usr/bin/python3
"""
build route by using flask
"""
from flask import Flask, render_template

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


@app.route("/c/<text>", strict_slashes=False)
def accParams(text):
    """
    Returns params that are passed on location
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonRoute(text):
    """
    Returns params that are passed on location
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def numberRoute(n):
    """
    Returns params that are passed on location
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n):
    """
    Returns params that are passed on location
    """
    return render_template('5-number.html', n=n)


@app.route("//number_odd_or_even/<int:n>", strict_slashes=False)
def evenOddTemplate(n):
    """
    Returns params that are passed on location
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
