from flask import Flask
from addiction.config import Config
from addiction.views.main.routes import main_blueprint
from addiction.views.auth.routes import auth_blueprint
from addiction.views.publications.routes import publication_blueprint
from addiction.extensions import db, migrate, login_manager, admin
from addiction.commands import init_db, populate_db
from addiction.models.user import User, Role
from addiction.models.staff import Staff
from addiction.models.file import File
from addiction.models.home import Home
from addiction.models.projects import Project
from addiction.adminpanel.models import SecureAdminView, UserModelView, StaffModelView, RoleModelView, FileModelView, HomeModelView, ProjectModelView

from flask_admin.base import MenuLink



BLUEPRINTS=[main_blueprint, auth_blueprint, publication_blueprint]
COMMANDS=[init_db, populate_db]


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    return app

def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view="auth.login"

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)
    
    admin.index_view=SecureAdminView()
    admin.init_app(app)
    admin.add_view(HomeModelView(Home, db.session))
    admin.add_view(StaffModelView(Staff, db.session))
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(RoleModelView(Role, db.session))
    admin.add_view(FileModelView(File, db.session))
    admin.add_view(ProjectModelView(Project, db.session))
    admin.add_link(MenuLink("Go back", url="/", icon_type="fa", icon_value="fa-sign-out"))



def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)