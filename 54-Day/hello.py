#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Welcome to web dev with flask")
