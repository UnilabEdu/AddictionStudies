from addiction.extensions import db
from addiction.models.base import BaseModel

class Project(BaseModel):

    __tablename__ = 'projects'

    id=db.Column(db.Integer, primary_key=True)
    current=db.Column(db.String)
    implemented=db.Column(db.String)