#!/usr/bin/env python3
from post import Post
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    post = Post()
    posts = post.fetch_all()
    return render_template("index.html", posts=posts)

@app.route("/post/<int:_id>")
def post(_id):
    post = Post()
    post = post.fetch_by_id(_id)
    return render_template("post.html", post=post)

if  __name__ == "__main__":
    app.run(debug=True)

