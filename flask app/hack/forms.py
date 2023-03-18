from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, EmailField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Login")

class RegForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Length(min=4, max=64)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=32)])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=8, max=128)])
    submit = SubmitField("Register")
    
class SearchForm(FlaskForm):
    query = StringField(validators=[DataRequired()])
    submit = SubmitField('Search')
