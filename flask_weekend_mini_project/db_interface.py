from datetime import datetime
from flaskblog import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:flask_weekend_mini_project///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
	# PRIMARY KEY (id), 
	# UNIQUE (username), 
	# UNIQUE (email)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

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

    def interst_into_postdb(self):
        for post in posts:
            self.cursor.execute(''' INSERT INTO table (title,date_posted ,content) VALUES (title,date_posted ,content)''')
    
    def import_Post(self):
        results = []
        self.cursor.execute('''SELECT * FROM post;''')
        for title, date_posted, content in self.cursor.fetchall():
            results.append(Post(title, date_posted, content))
        return results
