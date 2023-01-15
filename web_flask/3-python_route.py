#!/usr/bin/python3
""" Start a basic Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    """display “C ” followed by the \
    value of the text variable \
    (replace underscore _ symbols with a space )
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<string:text>',  strict_slashes=False)
def pyth(text="is cool"):
    """ display “Python ”, followed by the value of the text"""
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
