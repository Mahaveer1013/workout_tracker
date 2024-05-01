from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import Length, EqualTo, DataRequired

class Register_Form(FlaskForm):
    username = StringField(label="Username :", validators=[Length(min=4,max=15), DataRequired()])
    email = EmailField(label="Email :", validators=[DataRequired()])
    password = PasswordField(label="Password :", validators=[Length(min=4,max=15), DataRequired()])
    confirm_password = PasswordField(label="Confirm_password :", validators=[EqualTo('password', message='Passwords must match'), DataRequired() ])
    submit = SubmitField(label="Submit")

class Login_Form(FlaskForm):
    username = StringField(label="Username :")
    password = PasswordField(label="Password :")
    submit = SubmitField(label="Submit")

