#!/usr/bin/env python3
from cafe_data import Cafe
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import URLField

app = Flask(__name__)
app.config["__SECRETKEY__"] = "__passcode__"
Bootstrap(app)

@app.route("/")
def index():
    """ serve response to home page request """
    return render_template("index.html")

@app.route("/cafes")
def cafe():
    """ Response to cafe route requests """
    cafe = Cafe()
    cafe_data = cafe.cafe_data
    return render_template("cafes.html", cafes=cafe_data)

@app.route("/add")
def add():
    """ Secret page to add data datastore """
    return u"Welcome to our secret page 😁"

if __name__ == "__main__":
    app.run(debug=True)
