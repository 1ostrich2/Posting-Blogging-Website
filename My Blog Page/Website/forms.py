from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(),])
    email = EmailField(label="Email", validators=[DataRequired(),])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Your password must be at least 8 characters long.")])
    submit = SubmitField(label="Register")

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(),])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class CreatePostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(5, 35)])
    content = TextAreaField(label="Description", validators=[DataRequired(), Length(10, 500)])
    attachment = FileField(label="Upload Attachment")
    submit = SubmitField(label="Post")

class DeletePostForm(FlaskForm):
    submit = SubmitField(label="Delete")

class AddCommentForm(FlaskForm):
    content = StringField(label="Description", validators=[DataRequired(), Length(1, 500)])
    submit = SubmitField(label="Post")

class ChangeDisplayNameForm(FlaskForm):
    new_display_name = StringField(label="New Display Name", validators=[DataRequired(),])
    password = PasswordField(label="Password", validators=[DataRequired(),])
    submit = SubmitField(label="Confirm")

class ChangePasswordForm(FlaskForm):
    password = PasswordField(label="Old Password", validators=[DataRequired(),])
    new_password = PasswordField(label="New Password", validators=[DataRequired(), Length(min=8, message="Your password must be at least 8 characters long.")])
    submit = SubmitField(label="Confirm")

