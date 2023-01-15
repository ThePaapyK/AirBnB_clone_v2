#!/usr/bin/python3
""" Start a basic Flask web application"""

from flask import Flask
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>',  strict_slashes=False)
def pyth(text="is cool"):
    """ display “Python ”, followed by the value of the text"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n=None):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n=None):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int: n>', strict_slashes=False)
def even_or_odd(n=None):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
