from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, DecimalField
from wtforms.validators import InputRequired, Email


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = StringField('password', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email()])
    phone_number = StringField('phone_number', validators=[InputRequired()])
    profile_photo = FileField('profile_photo', 
                        validators=[FileAllowed(['jpg','jpeg', 
                                'png', 'Only images are accepted!'])])


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = StringField('password', validators=[InputRequired()])

