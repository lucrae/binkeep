import string, random
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256)) # hash
    is_superuser = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, is_superuser=False):
        self.username = username
        self.email = email
        self.is_superuser = is_superuser

    def __repr__(self):
        return "<User({}, {}, {})>".format(self.id, self.username, self.email)

    def get_admin_info(self):
        return {
            "id": self.id, 
            "username": self.username, 
            "email": self.email, 
            "password [hash]": self.password, 
            "is_superuser": self.is_superuser,
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32), unique=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(128)) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow) # hash
    is_private = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('collections', lazy='dynamic'))

    def __init__(self, title, description, user_id, is_private=False):
        self.title = title
        self.description = description
        self.is_private = is_private
        self.user_id = user_id

    def __repr__(self):
        return "<Collection({}, {}, {}, {})>".format(self.id, self.token, self.title, self.user_id, self.is_private)

    def get_admin_info(self):
        return {
            "id": self.id, 
            "token": self.token,
            "title": self.title, 
            "timestamp [utc]": self.timestamp.strftime('%Y-%m-%d %H:%M'), 
            "is_private": self.is_private,
            "author": self.author,
        }

    def set_token(self, length=8):
        self.token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))