#!/usr/bin/python3
""" starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session \
    after each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_n_cities():
    """display a HTML page: (inside the tag BODY)"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
