#!/usr/bin/env python3
import requests
from flask import Flask, render_template

api_endpoint = "https://api.npoint.io/1bfdbd4fe4fc82cf75f4"
res = requests.get(url=api_endpoint)
posts = res.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    post = posts[id - 1]
    return render_template("post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

