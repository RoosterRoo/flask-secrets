from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email("Please input a valid email id")])
    password = PasswordField(label='Password', validators=[InputRequired(), Length(8)])
    submit = SubmitField(label="Submit")
