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


@app.route('/c/<text>', strict_slashes=False)
def text():
    """display “C ” followed by the \
    value of the text variable \
    (replace underscore _ symbols with a space )
    """
    return 'C %s'.replace('_', ' ') % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
