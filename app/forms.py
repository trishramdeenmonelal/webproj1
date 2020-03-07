from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname  = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])
    