#!/usr/bin/python3
"""This scripts opens a basic Flask server with a list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list_page(id=None):

    return render_template("9-states.html", db=storage.all(State), id=id)


@app.teardown_appcontext
def teardown_db(close):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
