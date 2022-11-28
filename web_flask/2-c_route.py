#!/usr/bin/python3
"""Import flask and print with method"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """print Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """print HBNB in /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def HBNB_text(text):
    """print HBNB in /hbnb"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
