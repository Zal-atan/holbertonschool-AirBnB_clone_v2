#!/usr/bin/python3
"""This scripts opens a basic Flask server with one page"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def dashboard():

    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
