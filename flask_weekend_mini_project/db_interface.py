from datetime import datetime
from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    image = db.Column(db.LargeBinary, nullable=True)


    # PRIMARY KEY (id),
    # UNIQUE (username),
    # UNIQUE (email)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # PRIMARY KEY (id),
    # FOREIGN KEY(user_id) REFERENCES user (id)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

def create_db():
    db.create_all()


def add_user():
    admin = User(username='user', email='other@example.com',password='12334')
    db.session.add(admin)
    db.session.commit()


def dump_users():
    print(User.query.all())


def added_post():
    user = User.query.filter_by(username='admin').first()
    post = Post(title='how to have fun', content='Some text')
    user.posts.append(post)
    db.session.add(post)
    db.session.commit()
    print(Post.query.all())
    print(User.query.all())
    print(user.posts)


def get_all_users():
    # user = User.query.filter_by(username='admin')
    # print("user posts : ", user.posts)
    # posts = Post.query.all()
    # load_db()
    users = User.query.all()
    print(print(users))
    return users

if __name__ == '__main__':
    create_db()
    add_user()
    #print(get_all_users())