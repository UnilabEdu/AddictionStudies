from flask import Blueprint, render_template, current_app
from addiction.models.staff import Staff
from flask_login import login_required
import os


main_blueprint=Blueprint('main', __name__, template_folder="templates")
name_dict={"academic": "აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}


@main_blueprint.route("/")
def index():
    return render_template("main/index.html", name_dict=name_dict)


@main_blueprint.route("/projects")
@login_required
def projects():
    return render_template("main/projects.html", name_dict=name_dict)

@main_blueprint.route("/about")
def about():
    staff=Staff.query.all()
    return render_template("main/about.html", staff=staff, name_dict=name_dict)




