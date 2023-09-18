from flask import Flask, render_template, redirect, request, url_for
from flask_admin.menu import MenuLink

from addiction.config import Config
from addiction.extensions import db, login_manager, migrate, mail
from addiction.views import main_blueprint, auth_blueprint, publication_blueprint
from addiction.commands import init_db, populate_db
from addiction.admin import admin, SecureModelView, ProjectView, HomeView, PublicationView, StaffView, CategoryView, UserView
from addiction.models import User, Staff, Project, HomePageText, Publication, PublicationCategory


BLUEPRINTS = [
    main_blueprint,
    auth_blueprint,
    publication_blueprint
]

COMMANDS = [
    init_db,
    populate_db
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extensions(app)
    register_blueprints(app)
    register_commands(app)
    configure_error_handlers(app)

    return app


def initialize_extensions(app):
    # Flask-SQLAlchemy
    db.init_app(app)

    # # Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('auth.login', next=request.path))

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Mail
    mail.init_app(app)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(UserView(User, db.session, name="მომხმარებლები"))
    admin.add_view(HomeView(HomePageText, db.session, name="მთავარი"))
    admin.add_view(ProjectView(Project, db.session, name="პროექტები"))
    admin.add_view(CategoryView(PublicationCategory, db.session, name="რესურსები"))
    admin.add_view(StaffView(Staff, db.session, name="ჩვენს შესახებ"))
    admin.add_view(PublicationView(Publication, db.session, name="პუბლიკაციები"))
    admin.add_link(MenuLink("გამოსვლა", url="/logout", icon_type="fa", icon_value="fa-sign-out"))


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def configure_error_handlers(app):
    pass