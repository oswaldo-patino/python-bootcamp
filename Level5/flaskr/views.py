from flask import Flask, request
from flask.templating import render_template

from . import app

@app.route("/")
def home():
    return render_template("home.html")