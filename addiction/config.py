import os


class Config(object):
    PROJECT = "Addiction Studies"
    PROJECT_NAME = "Addiction Studies"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "TEMPORARY_SECRET_KEY"
    CSRF_ENABLED = True

    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    if os.environ.get('FLASK_DB') == "local":
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'db.sqlite')
    elif os.environ.get("FLASK_DB") == "prod":
        SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@0.0.0.0/public'

    # Flask-Admin
    FLASK_ADMIN_SWATCH = 'united'


class Constants(object):

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SERIALIZER_SALT = 'TEMPORARY_SERIALIZER_SALT'
    PUBLICATIONS_FOLDER = os.path.join(PROJECT_ROOT, "static", "publications")
    IMAGES_FOLDER = os.path.join(PROJECT_ROOT, "static", "images")
