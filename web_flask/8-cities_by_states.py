#!/usr/bin/python3
"""import flask to start the flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def closeSession(self):
    """
    close session from the db
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_and_city():
    """
    parse states and city in to template
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
