#!/usr/bin/env python3
import requests
from sendmail import SendMail
from flask import Flask, render_template, request

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

@app.route("/contact", methods=["get", "post"])
def contact():
    method = request.method
    if request.method == "POST":
        message = f"""
            Name: {request.form['name']}
            Email: {request.form['email']}
            Number: {request.form['num']}
            Message: {request.form['text']}
        """
        SendMail(msg=message)
    return render_template("contact.html", method_type=method)

if __name__ == "__main__":
    app.run(debug=True)

