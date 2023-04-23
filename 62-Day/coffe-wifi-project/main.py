#!/usr/bin/env python3
from cafe_data import Cafe
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap4
from cafe_wtform import CafeForm

app = Flask(__name__)
app.secret_key = "__passwd__"
bootstrap = Bootstrap4(app)

__filename = "cafe_csv_data.csv"

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

@app.route("/add", methods=["GET", "POST"])
def add():
    """ Secret page to add data datastore """
    cafe = Cafe()
    form = CafeForm()
    if form.validate_on_submit():
        data = form.data
        del data["csrf_token"], data["submit"]
        cafe.cafe_data = data
        return redirect(url_for("cafe"))
    return render_template("add.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)