from os import path

class Config(object):
    SECRET_KEY='jkdhsakhdiwuerhfkjfaksdhkuy1874626ty8gfeilahsasd'
    BASE_DIR=path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///'+path.join(BASE_DIR, 'db.sqlite')

    FLASK_ADMIN_SWATCH='united'
