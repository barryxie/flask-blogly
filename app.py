"""Blogly application."""
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post, Tag

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
    posts = Post.query.filter_by(user_id = user_id).all()
    return render_template('details.html', user=user, posts=posts)   


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


@app.route("/users/<int:user_id>/post/new")
def create_new_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('post.html', user=user) 


@app.route("/users/<int:user_id>/post/new", methods=['POST'])
def add_new_post(user_id):
    title = request.form['title']
    content = request.form['content']
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/posts/{new_post.id}') 

@app.route("/posts/<int:post_id>")
def show_post(post_id):
     post = Post.query.get(post_id)
     return render_template('post_detail.html', post=post)  

@app.route("/posts/<int:post_id>/edit")
def show_edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html',post=post)

@app.route("/posts/<int:post_id>/edit", methods=['POST'])
def create_edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content= request.form['content']

    db.session.add(post)
    db.session.commit()

    return redirect(f'/posts/{post.id}') 

@app.route("/posts/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')   


@app.route("/tags")
def tags_list():
    tags = Tag.query.all()
    return render_template('tags.html', tags=tags) 

@app.route("/tags/<int:tag_id>")
def tags_detail(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('tag.html', tag = tag)     

@app.route("/tags/new")
def create_tags_form():
    return render_template('new_tag.html') 


@app.route("/tags/new", methods=['POST'])
def create_tags():
    name = request.form['name']
    tag = Tag(name=name)

    db.session.add(tag)
    db.session.commit()

    return redirect('/tags')

@app.route("/tags/<int:tag_id>/edit")
def edit_tags_form(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('edit_tag.html', tag = tag)   


@app.route("/tags/<int:tag_id>/edit", methods=['POST'])
def edit_tags(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']

    db.session.add(tag)
    db.session.commit()

    return redirect(f'/tags/{tag.id}')    


@app.route("/tags/<int:tag_id>/delete", methods=['POST'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')                                



