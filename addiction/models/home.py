from addiction.extensions import db
from addiction.models.base import BaseModel


class HomePageText(BaseModel):
    __tablename__ = 'home_page_texts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return f"{self.id} - {self.name}"
    
    @classmethod
    def get_texts_categorized(cls):
        texts = cls.query.all()
        text_dict = {}
        category_map = {
            "ინსტიტუტის შესახებ": "about_institute",
            "მუშაობის მიმართულებები": "work_directions",
            "ინსტიტუტის შექმნის ისტორია": "institute_history"
        }

        for text in texts:
            text_category = category_map[text.category]
            if text_category in text_dict:
                text_dict[text_category].append(text)
            else:
                text_dict[text_category] = [text]
        return text_dict