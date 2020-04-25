'''
Uses flask_wtf, en extension for Flask, for generating forms ans usage in the app.
'''


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length

# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

    fullname = TextField(
        'Full Name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )

    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class TokenizerForm(Form):
    text = TextField('Input Text', [DataRequired()])

class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )


class AddServiceForm(Form):
    serviceName = TextField(
        'Service Name', validators=[DataRequired(), Length(min=2, max=25)]
    )
    serviceAuthor = TextField(
        'Service Author', validators=[DataRequired(), Length(min=3, max=40)]
    )

    servicePageCall = TextField(
        'Service page call', validators=[DataRequired(), Length(min=2, max=25)]
    )

    serviceServiceCall = TextField(
        'Service call', validators=[DataRequired(), Length(min=2, max=25)]
    )

    serviceAPIEndpoint = TextField(
        'Service endpoint', validators=[DataRequired(), Length(min=2, max=25)]
    )

    serviceTags = TextField(
        'Service tags', validators=[DataRequired(), Length(min=2, max=25)]
    )
