'''
Class for User data in database. Inherits from SQL-Alchemy base model for enabling usage of database elements into python code.
'''

from . import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    user_type = db.Column(db.String(30))
    fullname = db.Column(db.String(120), unique=False)

    def __init__(self, name=None, password=None, email=None, fullname = None, user_type = None):
        self.name = name
        self.email = email
        self.password = password
        self.fullname = fullname
        self.user_type = user_type


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class Service(db.Model):

    __tablename__ = 'Services'

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(120), unique=True)
    service_author = db.Column(db.String(120), unique=False)
    service_page_call = db.Column(db.String(120), unique=True)
    service_service_call = db.Column(db.String(120), unique=True)
    service_api_endpoint = db.Column(db.String(120), unique=True)
    service_tags = db.Column(db.String(120), unique=False)
