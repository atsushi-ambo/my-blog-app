# Import necessary modules
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy with the database URI
# The DATABASE_URL environment variable should contain the connection string for your MySQL server
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the User model
# This represents the Users table in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username of the user
    password = db.Column(db.String(120), nullable=False)  # Hashed password of the user
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email address of the user
    posts = db.relationship('Post', backref='author', lazy=True)  # Posts created by the user
    comments = db.relationship('Comment', backref='author', lazy=True)  # Comments created by the user

# Define the Post model
# This represents the Posts table in the database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each post
    title = db.Column(db.String(120), nullable=False)  # Title of the post
    content = db.Column(db.Text, nullable=False)  # Content of the post
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # When the post was created
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ID of the user who created the post
    comments = db.relationship('Comment', backref='post', lazy=True)  # Comments on the post

# Define the Comment model
# This represents the Comments table in the database
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each comment
    content = db.Column(db.Text, nullable=False)  # Content of the comment
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # When the comment was created
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # ID of the user who created the comment
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)  # ID of the post the comment is on

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    user = User(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201

# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    title = request.json.get('title')
    content = request.json.get('content')
    user_id = request.json.get('user_id')
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify({'id': post.id}), 201

# Endpoint to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts])

# Endpoint to get a single post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

# Endpoint to create a new comment
@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    content = request.json.get('content')
    user_id = request.json.get('user_id')
    comment = Comment(content=content, user_id=user_id, post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'id': comment.id}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
