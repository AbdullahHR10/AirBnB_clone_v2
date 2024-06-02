#!/usr/bin/python3
"""A simple Flask web application with 7 routes"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route that returns 'C ' followed by the value of the text variable.
    Replaces underscores with spaces."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Rotue that returns 'Python ' followed by the value of the text variable.
    Replaces underscores with spaces."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """that returns 'n is a number' only if n is an integer."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Route that displays an HTML page only if n is an integer."""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Route that displays an HTML page only if n is an integer.
    The page displays whether the number is even or odd."""
    return render_template('number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
