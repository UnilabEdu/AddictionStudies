from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length

class UploadForm(FlaskForm):
    pdf=FileField(validators=[ FileAllowed ( ["pdf"]), DataRequired()])
    image=FileField(validators=[ FileAllowed ( ['png', 'jpg', 'jpeg']), DataRequired()])
    displayname=StringField("მიუთითე დოკუმენტის სახელი (სავალდებულო)", validators=[DataRequired(), length(min=3, max=500)])
    folder=StringField("მიუთითე ფოლდერის სახელი  (სავალდებულო)", validators=[DataRequired(), length(min=3, max=500)])