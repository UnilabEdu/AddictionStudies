from addiction.extensions import db
from addiction.models.base import BaseModel


class Staff(BaseModel):
    __tablename__ = 'staff_members'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    position = db.Column(db.String)

    def __repr__(self):
        return f"{self.name}"
