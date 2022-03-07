from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me',default=False)
    submit = SubmitField('Login')


class Logout(FlaskForm):
    submit = SubmitField('Logout')


class PhotoForm(FlaskForm):
    # to allow file upload need following in form html: enctype = "multipart/form-data"
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!',)])
    # photo = FileField(validators=[FileRequired()])
    # submit = SubmitField('Upload')


class CommentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    # submit = SubmitField('Post')