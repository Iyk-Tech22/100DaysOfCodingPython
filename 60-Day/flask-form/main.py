#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def recieve_data():
    """ process contact requests """
    if request.method == "POST":
        name = request.form["fname"]
        pwd = request.form["pass"]
        return f"<h2> Data, Recieved  </h2>\
                <h2> Your name is {name}</h2>\
                <h2>Your password is {pwd}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
