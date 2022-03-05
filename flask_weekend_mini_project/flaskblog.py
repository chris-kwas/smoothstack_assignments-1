from multiprocessing import connection
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

from db_interface import User, Post
from forms import RegistrationForm, LoginForm
from flask import request, make_response ,session, Response
#from db_interface import get_all_users

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]
# users = [
#      {
#          'username': 'Corey Schafer',
#          'email': 'email 1',
#      },
#      {
#          'username': 'Jane Doe',
#          'email': 'email 2',
#      }
# ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=Post.query.all())


@app.route("/admin")
def admin():
    return render_template('admin.html', users=User.query.all())


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    user=User(username=form.username.data, email=form.email.data, password=form.password.data)
    print("asdsad", user.query.filter_by(username=form.username.data))
    if form.validate_on_submit() and user.query.filter_by(username=form.username.data).first() == None and user.query.filter_by(email=form.email.data).first() == None:
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            flash('You have been logged in!', 'success')
            if form.email.data == 'admin@blog.com':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('login'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
# @app.route('/cookie', methods=['GET','POST'])  
# def visit():
#     #cookies is a dictionary
#     #.get asks for specificed key(visit-count) if key doesnt exists creates it and sets value to second value (0)
#     visit_count=request.cookies.get('visit-count', 0)#return string
#     message =  "This is visit number {} ".format({int(visit_count)})
#     resp = make_response(render_template('cookie.html', amt=message))#return http respose object
#     vscount = int(visit_count) + 1
#     resp.set_cookie('visit-count', str(vscount))#cookie values are strings
#     return resp



if __name__ == '__main__':
    app.run(debug=True)