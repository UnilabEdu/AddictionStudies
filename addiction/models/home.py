from addiction.extensions import db
from addiction.models.base import BaseModel

class Home(BaseModel):

    __tablename__ = 'home'

    id=db.Column(db.Integer, primary_key=True)
    about=db.Column(db.String)
    directions=db.Column(db.String)
    history=db.Column(db.String)

    def __repr__(self):
        return f"{self.name}"