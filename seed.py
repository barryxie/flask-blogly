"""Seed file to make sample data for db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of departments
u1 = User(first_name="Alan", last_name="Alda")
u2 = User(first_name="Joel", last_name="Burton")
u3 = User(first_name="Jane", last_name="Smith")


db.session.add_all([u1, u2, u3])

db.session.commit()


