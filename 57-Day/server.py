#!/usr/bin/env python3
import requests
from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    d = date.today()
    year = d.year
    val= random.randint(0,10)
    return render_template("index.html", num=val, year=year, author="Iyk Tech")

# CHALLENGES
@app.route("/blog")
def blog():
    res = requests.get(url="https://api.npoint.io/4d6c7799a0756990fcaa")
    jokes = res.json()
    return render_template("blog.html", data=jokes)

if __name__ == "__main__":
    app.run(debug=True)
