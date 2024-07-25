#!/usr/bin/python3
"""Module that starts a Flask web application."""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Displays 'Hello HBNB!' for the root url"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Displays 'HBNB' for the 'hbnb' url"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
