#!/usr/bin/python3
"""This scripts opens a basic Flask server with a list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states_list_page(id=None):

    return render_template("100-hbnb.html", states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown_db(close):
    storage.close()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)