from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, render_template, current_app
from werkzeug.security import generate_password_hash
from addiction.emails import create_key, send_email
from addiction.views.publications.forms import UploadForm
from werkzeug.utils import secure_filename
import os

name_dict={"academic":"აკადემიური პუბლიკაციები", "annual":"წლიური ანგარიშები", "books": "წიგნები", "prevention":"პრევენციის სახელმძღვანელოები", "psychoed":"ფსიქოგანათლება", "research":"კვლევითი ანგარიშები", "treatment":"მკურნალობის გზამკვლევები"}


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
    can_edit=True
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

    def after_model_change(self, form, model, is_created):
        if is_created:
            key=create_key(form.email.data)
            html=render_template('auth/_activation_message.html', key=key)
            send_email('ანგარიშის დადასტურება', html, form.email.data)
        
class StaffModelView(SecureModelView):
    column_searchable_list=['name', 'email']
    column_editable_list=['position']


class RoleModelView(SecureModelView):
    can_create=False
    can_edit=False

class FileModelView(SecureModelView):
    can_create=True
    column_exclude_list=['filename']
    can_edit = True
    can_delete = True
    column_searchable_list = ['displayname']
    column_filters = ['category']
    form = UploadForm

    def on_model_change(self, form, model, is_created):
        if form.pdf.data and form.image.data:
            filename = secure_filename(form.pdf.data.filename)
            image=secure_filename(form.image.data.filename)
            category=name_dict[model.folder]
            path = os.path.join(current_app.config['BASE_DIR'], 'static', 'publications', model.folder, filename)
            image_path = os.path.join(current_app.config['BASE_DIR'], 'static', 'images', image)
            form.pdf.data.save(path)
            form.image.data.save(image_path)
            model.filename = filename
            model.image=image
            model.category=category

class HomeModelView(SecureModelView):
    can_delete=False

class ProjectModelView(SecureModelView):
    can_delete=False

    
