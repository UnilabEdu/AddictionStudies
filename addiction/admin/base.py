from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next="/admin"))


class SecureIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')

    def is_visible(self):
        return False

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login', next="/admin"))
