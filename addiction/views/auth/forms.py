
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, length, equal_to, Email, ValidationError
from addiction.models.user import User
from sqlalchemy import or_


class RegisterForm(FlaskForm):
    email = EmailField('ელფოსტა',[DataRequired(), Email()])
    username=StringField("მომხმარებლის სახელი", validators=[DataRequired()])
    password=PasswordField("პაროლი", validators=[DataRequired(), length(min=8, max=16)])

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("ამ სახელით მომხმარებელი უკვე დარეგისტრირებულია")
    
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("ამ ელფოსტით მომხმარებელი უკვე დარეგისტრირებულია")


class LoginForm(FlaskForm):
    login = StringField("მომხმარებლის სახელი ან ელფოსტა", [DataRequired()])
    password = PasswordField("პაროლი", [DataRequired()])
    submit = SubmitField('შესვლა')
    

    def validate_password(self, password):
        user = User.query.filter(or_(User.email == self.login.data, User.username == self.login.data)).first()

        if not user:
            raise ValidationError("მომხმარებლის სახელი ან ელფოსტა არასწორია")
        if not user.check_password(password.data):
            raise ValidationError("პაროლი არასწორია")

class RecoveryForm(FlaskForm):
    email = EmailField('შეიყვანეთ ელფოსტა',[DataRequired(), Email()])
    submit = SubmitField('დადასტურება')

class ResetPasswordForm(FlaskForm):
    password=PasswordField("ახალი პაროლი", validators=[DataRequired("პაროლი სავალდებულოა"), length(min=8, max=16)])
    confirm_password=PasswordField("დაადასტურეთ პაროლი", validators=[DataRequired("პაროლის დადასტურება სავალდებულოა"), equal_to("password", message="პაროლები არ ემთხვევა ერთმანეთს")])
    submit=SubmitField('პაროლის აღდგენა')



    