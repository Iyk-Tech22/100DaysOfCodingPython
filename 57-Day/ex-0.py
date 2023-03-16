#!/usr/bin/env python3
import requests
from flask import Flask, render_template

agify_endpoint = "https://api.agify.io"
ged_endpoint = "https://api.genderize.io"

app = Flask(__name__)

@app.route("/guess/<name>")
def guess(name):
    params = {
        "name":name
    }

    agify_res = requests.get(url=agify_endpoint, params=params)
    ged_res = requests.get(url=ged_endpoint, params=params)
    
    age = agify_res.json()["age"]
    gender = ged_res.json()["gender"]
    
    return render_template("ex-0.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
