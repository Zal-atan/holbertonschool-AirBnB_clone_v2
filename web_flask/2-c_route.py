#!/usr/bin/python3
"""This scripts opens a basic Flask server with two pages"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def dashboard():

    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():

    return ("HBNB")


@app.route("/c/<text>")
def variable_page(text):

    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
