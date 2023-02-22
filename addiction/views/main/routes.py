from flask import Blueprint, render_template, current_app, flash, session
from flask_login import current_user
from addiction.models.staff import Staff
from addiction.models.home import Home
from addiction.models.projects import Project
from flask_login import login_required
import os



main_blueprint=Blueprint('main', __name__, template_folder="templates")

@main_blueprint.before_app_request
def email_not_confirmed():
    if current_user.is_authenticated and not current_user.confirmed:
        flash("თქვენ არ გაქვთ მეილი დადასტურებული. ანგარიშის გასააქტიურებლად შეამოწმეთ ელფოსტა. თუ მეილს ვერ პოულობთ, მოითხოვეთ ხელახლა გაგზავნა ")
    elif current_user.is_authenticated and current_user.confirmed:
        flash("თქვენი ელფოსტა წარმატებით დადასტურდა!")
name_dict={"academic": "აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}


@main_blueprint.route("/")
def index():
    home=Home.query.all()
    abt=[]
    dr=[]
    for i in home:
        abt.append(i.about)
        dr.append(i.directions)
     
    return render_template("main/index.html", name_dict=name_dict, home=home, abt=abt, dr=dr)


@main_blueprint.route("/projects")
def projects():
    projects=Project.query.all()
    return render_template("main/projects.html", name_dict=name_dict, projects=projects)

@main_blueprint.route("/about")
def about():
    staff=Staff.query.all()
    return render_template("main/about.html", staff=staff, name_dict=name_dict)




