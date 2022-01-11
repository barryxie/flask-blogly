"""Seed file to make sample data for db."""

from models import User, Post, db
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

p1 = Post(title="title1", content="content1", user_id=1)
p2 = Post(title="title2", content="content2", user_id=1)
p3 = Post(title="title3", content="content3", user_id=1)
p4 = Post(title="title4", content="content4", user_id=2)
p5 = Post(title="title5", content="content5", user_id=2)
p6 = Post(title="title6", content="content6", user_id=3)

db.session.add_all([p1, p2, p3,p4,p5,p6])

db.session.commit()


