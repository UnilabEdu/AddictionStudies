from flask import Blueprint, render_template, current_app
from flask_login import login_required
from addiction.models.file import File
import os
from addiction.views.publications.forms import UploadForm
from werkzeug.utils import secure_filename


publication_blueprint=Blueprint('publication', __name__, template_folder="templates")
name_dict={"academic":"აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}


@publication_blueprint.route("/publications/<string:folder>", methods=['GET', 'POST'])
def publication(folder):
    publications=File.query.filter_by(folder=folder).all()
    form=UploadForm()
    if form.validate_on_submit():
        if form.pdf.data:
            filename=secure_filename(form.pdf.data.filename)
            displayname=form.displayname.data
            path=os.path.join(current_app.config['BASE_DIR'], 'static', 'publications', folder, filename)
            form.pdf.data.save(path)
            new_file=File(filename=filename, displayname=displayname, file_path=path, folder=folder)
            new_file.create()
    return render_template("publications/publications.html", publications=publications, name_dict=name_dict, folder=folder, form=form)




@publication_blueprint.route('/view/<pdf_name>')
def view(pdf_name):
     publication=File.query.filter_by(filename=pdf_name).first()
     return render_template("publications/closeview.html", publication=publication, name_dict=name_dict)

