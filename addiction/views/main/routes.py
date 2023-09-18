from flask import Blueprint, render_template

from addiction.models import Project, Staff, HomePageText, PublicationCategory

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def index():
    texts = HomePageText.get_texts_categorized()
    return render_template("main/index.html", texts=texts)


@main_blueprint.route("/projects")
def projects():
    finished_projects = Project.query.filter_by(is_finished=True).all()
    unfinished_projects = Project.query.filter_by(is_finished=False).all()
    return render_template("main/projects.html", unfinished_projects=unfinished_projects, finished_projects=finished_projects)


@main_blueprint.route("/about_us")
def about():
    staff_members = Staff.query.all()
    return render_template("main/about_us.html", staff_members=staff_members)


@main_blueprint.route("/resources")
def resources():
    categories = PublicationCategory.query.all()
    return render_template("main/resources.html", categories=categories)



