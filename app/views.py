"""
This file contains all the routes for our application. This will tell Flask what to display on which path.

Flask provides a method, render_template,
which we can use to specifiy which HTML file should be loaded in a particular view.
"""

from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
