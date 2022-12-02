#!/usr/bin/python3
"""Import flask and print with method"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def state_list(n=None):
    """return all state"""
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
