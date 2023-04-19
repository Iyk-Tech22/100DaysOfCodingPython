#!/usr/bin/env python3
""" Simple Web app with Flask """
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "__passwd__"

#WTFORMS GENERATING
class Forms(FlaskForm):
    """ Generate forms fielda dynamicly """
    email = StringField(label="Your Email", validators=[DataRequired(), Email()])
    passwd = PasswordField(label="Your Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Forms()
    if form.validate_on_submit():
        email = form.email.data
        pwd = form.passwd.data
        if email == "admin@email.com" and pwd == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
