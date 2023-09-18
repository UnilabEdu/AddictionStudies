from addiction.extensions import db
from addiction.models.base import BaseModel


class Publication(BaseModel):
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    filename = db.Column(db.String)
    imagename = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey("publication_categories.id"))
    category = db.relationship("PublicationCategory")

    def get_image(self):
        return f"images/{self.imagename}"

    def get_file(self):
        return f"publications/{self.filename}"


class PublicationCategory(BaseModel):
    __tablename__ = 'publication_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name