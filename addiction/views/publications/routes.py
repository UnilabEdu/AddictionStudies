from flask import Blueprint, render_template
from flask_login import login_required
from flask import send_from_directory, abort, current_app
from addiction.models.file import File
import os

publication_blueprint=Blueprint('publication', __name__, template_folder="templates")

@publication_blueprint.route("/academic")
def academic():
    academic_publications=File.query.filter_by(category="academic").all()
    # for i in academic_publications:
    #     print(i.displayname)
    return render_template("publications/academic.html", academic_publications=academic_publications)

@publication_blueprint.route("/annual")
def annual():
    annual_publications=File.query.filter_by(category="annual").all()
    return render_template("publications/annual.html", anual_publications=annual_publications)

@publication_blueprint.route("/books")
def books():
    books=File.query.filter_by(category="books").all()
    return render_template("publications/books.html", books=books)


@publication_blueprint.route("/prevention")
def prevention():
    prevention=File.query.filter_by(category="prevention").all()
    return render_template("publications/prevention.html", prevention=prevention)

@publication_blueprint.route("/psychoed")
def psychoed():
    psychoed=File.query.filter_by(category="psychoed").all()
    return render_template("publications/psychoed.html", psychoed=psychoed)

@publication_blueprint.route("/research")
def research():
    research=File.query.filter_by(category="research").all()
    return render_template("publications/research.html", research=research)

@publication_blueprint.route("/treatment")
def treatment():
    treatment=File.query.filter_by(category="treatment").all()
    return render_template("publications/treatment.html", treatment=treatment)

@publication_blueprint.route('/view/<pdf_name>')
def view(pdf_name):
     publication=File.query.filter_by(filename=pdf_name).first()
     return render_template("publications/closeview.html", publication=publication)


@publication_blueprint.route("/get_file/<pdf_name>")
def get_file( pdf_name):
    relative='static/publications'
    incomplete_path=os.path.join(current_app.config['BASE_DIR'], relative)
    file=File.query.filter_by(filename=pdf_name).first()
    try:
        return send_from_directory(os.path.join(incomplete_path, file.category), pdf_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)
