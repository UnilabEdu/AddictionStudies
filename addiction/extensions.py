from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_mail import Mail
from addiction.adminpanel.models import SecureAdminView

db=SQLAlchemy()
migrate=Migrate()
login_manager=LoginManager()
mail=Mail()
admin=Admin(name="addiction studies", template_mode='bootstrap4', index_view=SecureAdminView())