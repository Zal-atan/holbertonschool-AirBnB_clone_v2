#!/usr/bin/python3
"""This scripts opens a basic Flask server with a list of states"""
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list_page():

    return render_template("7-states_list.html", db=storage.all(State))


@app.teardown_appcontext
def teardown_db(close):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
