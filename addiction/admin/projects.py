from wtforms.fields import TextAreaField, SelectField

from addiction.admin import SecureModelView


class ProjectView(SecureModelView):
    form_overrides = dict(description=TextAreaField, is_finished=SelectField)
    form_args = dict(is_finished={"choices": [(True, "დასრულებული"), (False, "მიმდინარე")]})

    column_labels = dict(year="წელი", title="სახელი", description="აღწერა", is_finished="სტატუსი")
    column_formatters = dict(is_finished=lambda v, c, m, n: "დასრულებული" if m.is_finished else "მიმდინარე")
