from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import SubmitField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, length

class UploadForm(FlaskForm):
    pdf=FileField(validators=[ FileAllowed ( ["pdf"])])
    upload=SubmitField('upload')
    displayname=StringField("მიუთითე დოკუმენტის სახელი (სავალდებულო)", validators=[DataRequired("დოკუმენტის სახელი სავალდებულოა"), length(min=3, max=500)])
    category=StringField("მიუთითე ფოლდერის სახელი  (სავალდებულო)", validators=[DataRequired("ფოდელრის სახელი სავალდებულოა"), length(min=3, max=500)])