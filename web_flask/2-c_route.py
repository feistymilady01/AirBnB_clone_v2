#!/usr/bin/python3
"""
Starts a web application using a variable
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_Hbnb():
    """ Displays Hello HBNB """

    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Displays HBNB """

    return 'HBNB'


@app.route('/c/<text>')
def use_var(text):
    """ Displays C concatenated with <text> """

    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
