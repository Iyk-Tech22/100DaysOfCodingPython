from flask_wtf import FlaskForm
from wtforms import StringField, URLField
from wtforms.validators DataRequired

class CafeForm(FlaskForm):
    """ Defines Form Fields """
    cafe_name = StringField(label="Cafe Name", validate=[DataRequired()])
    location = StringField(label="Cafe Location Google Map(URL)", validate=[DataRequired()])
    _open = StringField(label="Opening Time (8AM)", validate=[DataRequired()])
    close = StringField(label="Close Time (8PM)", validate=[DataRequired()])
    rating = StringField(label="Coffe Rating", validate=[DataRequired()])
    wifi = StringField(label="Wifi Strength Rating", validate=[DataRequired()])
    power = StringField(label="Power Socket Rating", validate=[DataRequired()])
    submit = StringField(label="Submit", validate=[DataRequired()])


