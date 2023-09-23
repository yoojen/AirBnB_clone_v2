#!/usr/bin/python3
"""import flask to start the flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closeSession(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def listofstates():
    """
    returns the list of states
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

