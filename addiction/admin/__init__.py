from flask_admin import Admin

from addiction.admin.base import SecureIndexView, SecureModelView
from addiction.admin.projects import ProjectView
from addiction.admin.home import HomeView
from addiction.admin.publications import PublicationView
from addiction.admin.categories import CategoryView
from addiction.admin.staff import StaffView

admin = Admin(name="ადიქტოლოგიის ინსტიტუტი", template_mode='bootstrap4', index_view=SecureIndexView(), base_template="admin/admin_base.html")