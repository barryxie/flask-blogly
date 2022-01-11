"""Blogly application."""

from flask import Flask,request, render_template, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def home():
    
    return redirect("/users")

@app.route("/users")
def list_users():
    users = User.query.all()
    return render_template('index.html', users=users) 

@app.route("/users/new")
def add_user():
    return render_template('newuser.html')  

@app.route("/users/new", methods=['POST']) 
def create_new_user():
    first_name = request.form['first_name'] 
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = image_url if image_url else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)   

    db.session.add(new_user) 
    db.session.commit() 

    return redirect(f"/users/{new_user.id}")

@app.route("/users/<int:user_id>")
def show_user_detial(user_id): 
    user = User.query.get_or_404(user_id) 
    return render_template('details.html', user=user)   


@app.route("/users/<int:user_id>/edit")
def edit_user(user_id): 
       user = User.query.get_or_404(user_id) 
       return render_template('edit.html', user=user)


@app.route("/users/<int:user_id>/edit",  methods=['POST'])
def save_edit_user(user_id): 
       edit_user = User.query.get_or_404(user_id)
       edit_user.first_name = request.form['first_name'] 
       edit_user.last_name = request.form['last_name']
       edit_user.image_url = request.form['image_url']

       db.session.add(edit_user) 
       db.session.commit()  

       return redirect('/users')     

@app.route("/users/<int:user_id>/delete" ,  methods=['POST'])
def delele_user(user_id):
    user = User.query.get_or_404(user_id) 
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')     




