#!/usr/bin/python3
"""
Gets the State and the cities in a state as a list
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_session(self):
    """ Closes sqlalchemy session """

    storage.close()


@app.route('/cities_by_states')
def cities_in_state():
    """ Renders the 8-cities_by_states.html page """

    # cities = storage.all('City')
    states = storage.all('State')
    # print(states)
    return render_template(
            '8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
