from wtforms.fields import TextAreaField, SelectField

from addiction.admin import SecureModelView


class HomeView(SecureModelView):
    form_overrides = dict(text=TextAreaField, category=SelectField)
    form_args = dict(category={"choices": ["ინსტიტუტის შესახებ", "მუშაობის მიმართულებები", "ინსტიტუტის შექმნის ისტორია"]})

    column_labels = dict(name="სახელი", text="აღწერა", category="ველი")