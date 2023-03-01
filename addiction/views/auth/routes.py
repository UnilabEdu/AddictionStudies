from flask import Blueprint, render_template, redirect, url_for, request
from addiction.views.auth.forms import LoginForm, RecoveryForm, ResetPasswordForm
from addiction.models.user import User
from flask_login import login_user, logout_user, current_user
from addiction.emails import create_key, send_email, confirm_key
from sqlalchemy import or_




auth_blueprint=Blueprint('auth', __name__, template_folder='templates')
name_dict={"academic": "აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}


@auth_blueprint.route('/confirm_email/<string:key>')
def confirm_email(key):
    email=confirm_key(key)
    user=User.query.filter_by(email=email).first()
    if user and not user.confirmed:
        user.confirmed=True
        user.save()
        return redirect(url_for('main.index'))
    else:
        return "დაფიქსირდა შეცდომა"

@auth_blueprint.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
    form=RecoveryForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            user.reset_password=True
            reset_key=create_key(form.email.data)
            html=render_template('auth/_reset_message.html', key=reset_key)
            send_email('პაროლის აღდგენა', html, form.email.data)
            user.save()
            return "პაროლის აღდგენის ლინკი გამოგზავნილია თქვენს ელფოსტაზე"
    return render_template("auth/forgot_password.html", form=form)

@auth_blueprint.route("/reset_password/<string:key>", methods=['GET', 'POST'])
def reset_password(key):
    form=ResetPasswordForm()
    email=confirm_key(key)
    user=User.query.filter_by(email=email).first()
    if not user: 
        return 'დაფიქსირდა შეცდომა'
    if not user.reset_password:
        return "პაროლი აღდგენილია"
        
    
    if form.validate_on_submit():
        user.password=form.password.data
        user.reset_password=False
        user.save()
        return redirect(url_for('auth.login'))
    return render_template("auth/reset_password.html", form=form)




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