#!/usr/bin/python3
"""Import flask and print with method"""
from flask import Flask, render_template, request

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
    """print text variable and replace character"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """print text variable and replace character"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """print n if is integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """print html page if is integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """print html page if is integer"""
    if (n % 2) == 0:
        text = "{0} is Even".format(n)
        return render_template('6-number_odd_or_even.html', n=text)
    else:
        text = "{0} is Odd".format(n)
        return render_template('6-number_odd_or_even.html', n=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
