from flask_admin.form import FileUploadField, ImageUploadField
from flask_wtf.file import FileAllowed
from markupsafe import Markup

from addiction.admin import SecureModelView
from addiction.config import Constants


class PublicationView(SecureModelView):
    form_overrides = dict(filename=FileUploadField, imagename=ImageUploadField)
    form_args = dict(filename={"validators": [FileAllowed(["pdf"])],
                               "base_path": Constants.PUBLICATIONS_FOLDER,
                               "render_kw": {"accept": ".pdf"}},

                     imagename={"validators": [FileAllowed(["png", "jpg", "jpeg"])],
                                "render_kw": {"accept": ".png,.jpg,.jpeg"},
                                "base_path": Constants.IMAGES_FOLDER,
                                "url_relative_path": "images/"})

    column_list = ["imagename", "name", "category"]
    column_labels = dict(name="სახელი", imagename="სურათი", category="კატეგორია", filename="ფაილი")
    column_formatters = dict(imagename=lambda v, c, m, n: Markup(f"<img src=/static/{m.get_image()} "
                                                                    f"style='width: 125px; height: 150px; border-radius: 16px;'/>"))
