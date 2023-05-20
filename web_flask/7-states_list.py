#!/usr/bin/python3
"""
Gets all state and render as a list
"""

from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_session(self):
    """ Closes the sqlalchemy session """

    storage.close()


@app.route('/states_list')
def state_list():
    """  Renders the 7-states_list.html page """

    states = storage.all('State')
    # print(states)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
