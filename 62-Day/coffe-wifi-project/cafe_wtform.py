from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired

class CafeForm(FlaskForm):
    """ Defines Form Fields """
    CafeName = StringField("Cafe Name",  validators=[DataRequired()])
    Location = StringField("Cafe Location Google Map(URL)", [DataRequired()])
    Open = StringField("Opening Time (8AM)",  validators=[DataRequired()])
    Close = StringField("Close Time (8PM)",  validators=[DataRequired()])
    CoffeeRate = StringField("Coffe Rating",  validators=[DataRequired()])
    WifiRate = StringField("Wifi Strength Rating",  validators=[DataRequired()])
    PowerRate = StringField("Power Socket Rating",  validators=[DataRequired()])
    submit = SubmitField("Submit")


