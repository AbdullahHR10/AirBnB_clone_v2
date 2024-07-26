#!/usr/bin/python3
"""Module that starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays 'Hello HBNB!' for the root url"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Displays 'HBNB' for the 'hbnb' url"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """Displays “C ”, followed by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_is_cool(text='is_cool'):
    """Displays “Python ”, followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_number(n):
    """Displays “n is a number” only if n is an integer"""
    n = str(n)
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Displays a HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, parity='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, parity='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
