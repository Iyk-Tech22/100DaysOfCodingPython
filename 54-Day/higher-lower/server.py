#!/usr/bin/env python3
from flask import Flask
from random import randint

app = Flask(__name__)
actual_num = 5

@app.route("/")
def guess_game():
    global actual_num
    actual_num = randint(0, 9)
    return "<h2> Guess a number between 1 to 9</h2><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/guess/<int:num>")
def guess(num):
    if num > actual_num:
        return "<h2 style='color:purple'>     Too high, try again</h2><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num < actual_num:
        return "<h2 style='color:red'>Too     low, Try Again!</h2><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h2 style='color:green'>Correct you got me!</h2><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'><br/><a href='http://127.0.0.1:5000'> Play Again </a>"


        
if __name__ == "__main__":
    app.run(debug=True)
