from addiction.extensions import db
from addiction.models.base import BaseModel

class File(BaseModel):
    __tablename__='files'

    id=db.Column(db.Integer, primary_key=True)
    filename=db.Column(db.String(200))
    displayname=db.Column(db.String(200))
    folder=db.Column(db.String(200))
    category=db.Column(db.String(200))