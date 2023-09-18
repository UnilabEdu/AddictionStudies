from addiction.admin import SecureModelView


class CategoryView(SecureModelView):
    column_labels = dict(name="სახელი")
