from flask import Blueprint, render_template

from addiction.models import Publication

publication_blueprint = Blueprint('publications', __name__)


@publication_blueprint.route("/publications/<int:category_id>")
def publication(category_id):
    publications = Publication.query.filter_by(category_id=category_id).all()
    return render_template("publications/publications.html", publications=publications)




