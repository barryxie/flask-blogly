"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey
import datetime

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    def __repr__(self):
        u = self
        return f"<User id={u.id} {u.last_name} {u.first_name} >"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.Text, nullable=False)

    last_name = db.Column(db.Text, nullable=False)

    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_a = db.Column(db.DateTime, nullable=False,default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=backref('posts', cascade="all, delete-orphan"))
    

