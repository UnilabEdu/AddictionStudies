from os import path
from pathlib import Path


class Config(object):
    SECRET_KEY='jkdhsakhdiwuerhfkjfaksdhkuy1874626ty8gfeilahsasd'
    # BASE_DIR=Path(__file__).absolute().parent
    BASE_DIR=path.abspath(path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///'+path.join(BASE_DIR, 'db.sqlite')
    FLASK_ADMIN_SWATCH='united'


