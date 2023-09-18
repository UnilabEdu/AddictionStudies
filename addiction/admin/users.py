from flask_login import current_user
from wtforms import PasswordField

from addiction.admin import SecureModelView


class UserView(SecureModelView):
    form_extra_fields = {'new_password': PasswordField('Password')}
    form_columns = ["email", "username", "new_password", "role"]

    column_labels = dict(email="ელფოსტა", username="მომხმარებლის სახელი", password="პაროლი", role="როლი")
    column_exclude_list = ["_password", "reset_password"]

    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")

    def on_model_change(self, form, model, is_created):
        if form.new_password.data != "":
            model.password = form.new_password.data
