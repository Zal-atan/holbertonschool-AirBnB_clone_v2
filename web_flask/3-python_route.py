#!/usr/bin/python3
"""This scripts opens a basic Flask server with four pages"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def dashboard():

    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():

    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def variable_page(text):

    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False, defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_variable_page(text):

    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
