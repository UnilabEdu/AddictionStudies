from flask import Blueprint, render_template, redirect, url_for, request
from addiction.views.auth.forms import LoginForm
from addiction.models.user import User
from flask_login import login_user, logout_user, current_user
from sqlalchemy import or_




auth_blueprint=Blueprint('auth', __name__, template_folder='templates')
name_dict={"academic": "აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter(or_(User.username==form.login.data, User.email==form.login.data)).first()
        next=request.args.get("next")
        if user and user.check_password(form.password.data):
            login_user(user)
            if next:
                return redirect(next)
            else:
                return redirect(url_for("main.index"))
        else:
            print('couldnt login user')
    return render_template("auth/login.html", form=form, name_dict=name_dict)

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))