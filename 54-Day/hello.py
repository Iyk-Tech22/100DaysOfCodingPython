#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

# CHALLANGE::1
def make_bold(bye):
    def wrapper():
        return "<b>{}</b>".format(bye())
    return wrapper

def make_underline(bye):
    def wrapper():
        return "<u>{}</u>".format(bye())
    return wrapper

def make_emphasis(bye):
    def wrapper():
        return "<em>{}</em>".format(bye())
    return wrapper

@app.route("/bye")
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye"


@app.route("/")
def hello():
    return \
    "<h1>Welcome to web dev with flask</h1>"\
    "<p>We will talking about flasks</p>"\

@app.route("/username/<name>")
def greating(name):
    return f"Welcome back {name}"

@app.route("/age/<int:age>")
def age(age):
    return f"You are {age} years old"

if __name__ == "__main__":
    app.run(debug=True)
