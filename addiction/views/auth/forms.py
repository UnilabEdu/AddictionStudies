
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, equal_to

class RegisterForm(FlaskForm):
    username=StringField("მომხმარებლის სახელი", validators=[DataRequired("მომხმარებლის სახელი სავალდებულოა")])
    password=PasswordField("პაროლი", validators=[DataRequired("პაროლი სავალდებულოა"), length(min=8, max=16)])
    confirm_password=PasswordField("დაადასტურეთ პაროლი", validators=[DataRequired("პაროლის დადასტურება სავალდებულოა"), equal_to("password", message="პაროლები არ ემთხვევა ერთმანეთს")])
    submit=SubmitField('რეგისტრაცია')


class LoginForm(FlaskForm):
    username = StringField("მომხმარებლის სახელი", [DataRequired()])
    password = PasswordField("პაროლი", [DataRequired()])
    submit = SubmitField('შესვლა')



    