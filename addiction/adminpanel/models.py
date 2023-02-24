from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for
from werkzeug.security import generate_password_hash

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))

class SecureAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')
    
    def is_visible(self):
        return False
    
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login"))

class UserModelView(SecureModelView):
    can_create=True
    can_edit=False
    can_view_details=False
    column_searchable_list=['username']
    column_list=['username', 'roles']
    form_columns = ['email','username', 'password', 'roles']
    can_export=True

    def on_model_change(self, form, model, is_created):
        if is_created:
            password = form.password.data
            hashed_password = generate_password_hash(password)
            model._password = hashed_password


    

class StaffModelView(SecureModelView):
    column_searchable_list=['name', 'email']
    column_editable_list=['position']


class RoleModelView(SecureModelView):
    can_create=False
    can_edit=False

class FileModelView(SecureModelView):
    can_create=False
    column_exclude_list=['filename', 'file_path']

class HomeModelView(SecureModelView):
    can_delete=False

class ProjectModelView(SecureModelView):
    can_delete=False


    
