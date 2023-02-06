
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, equal_to

class RegisterForm(FlaskForm):
    username=StringField("მომხმარებლის სახელი", validators=[DataRequired("Username required")])
    password=PasswordField("პაროლი", validators=[DataRequired("Password equired"), length(min=8, max=16)])
    confirm_password=PasswordField("დაადასტურეთ პაროლი", validators=[DataRequired("Confirm password required"), equal_to("password", message="Passwords do not match")])
    submit=SubmitField('რეგისტრაცია')


class LoginForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", [DataRequired()])
    password = PasswordField("პაროლი", [DataRequired()])
    submit = SubmitField('შესვლა')



    