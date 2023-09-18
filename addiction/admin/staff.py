from wtforms.fields import TextAreaField

from addiction.admin import SecureModelView


class StaffView(SecureModelView):
    form_overrides = dict(position=TextAreaField)
    column_labels = dict(name="სახელი", email="ელ.ფოსტა", position="პოზიცია")
