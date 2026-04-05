from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class user_model(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(22), unique=True, nullable=False)
    display_name = db.Column(db.String(22), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    upvoted_posts = db.Column(db.String(), nullable=True)
    downvoted_posts = db.Column(db.String(), nullable=True)

    posts = db.relationship('post_model', backref='user_model')

    def get_id(self):
        return self.user_id

    def changeDisplayName(self, new_display_name):
        self.display_name = new_display_name

    def changePassword(self, new_password):
        self.password = new_password


class post_model(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(250), nullable=False)
    attachment = db.Column(db.String(250), nullable=True)
    
    upvote_count = db.Column(db.Integer, nullable=False)
    downvote_count = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.user_id'))
    
    comments = db.relationship('comment_model', backref='post_model')


class comment_model(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(50), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.user_id'))
    username = db.Column(db.String(22), db.ForeignKey('user_model.username'))
    display_name = db.Column(db.String(22), db.ForeignKey('user_model.display_name'))

    post_id = db.Column(db.Integer, db.ForeignKey('post_model.post_id'))
