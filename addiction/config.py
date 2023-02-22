from os import path, environ



class Config(object):
    SECRET_KEY=environ.get('SECRET_KEY')
    BASE_DIR=path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///'+path.join(BASE_DIR, 'db.sqlite')
    FLASK_ADMIN_SWATCH='united'
    
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class Constants:
    SERIALIZER_SALT='12345678'


