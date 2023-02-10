from addiction.extensions import db
from addiction.models.base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel, UserMixin):

    __tablename__="users"

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique=True)
    _password=db.Column("password", (db.String))
    roles=db.relationship('Role', secondary="user_roles")

    def __repr__(self):
        return f"{self.name}"
    
    def _get_password(self):
        return self._password
    
    def _set_password(self, password):
        self._password=generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def has_role(self, role):
        return role in [userrole.name for userrole in self.roles]
    
    password=db.synonym('_password', descriptor=property(_get_password, _set_password))

class UserRole(BaseModel):
    __tablename__='user_roles'
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))


class Role(BaseModel):
    __tablename__="roles"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, unique=True)

    def __repr__(self):
        return f"{self.name}"

