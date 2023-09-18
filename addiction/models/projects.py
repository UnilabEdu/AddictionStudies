from addiction.extensions import db
from addiction.models.base import BaseModel


class Project(BaseModel):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    is_finished = db.Column(db.Boolean)
