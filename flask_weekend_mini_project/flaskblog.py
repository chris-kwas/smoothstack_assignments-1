from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from db_interface import User, Post
from forms import RegistrationForm, LoginForm, Logout, CommentForm, PhotoForm
from flask import request, make_response ,session
#from db_interface import get_all_users

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024  # limit size of uploads

db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    if session.get('email'):
        flash(f"Logged in, Welcome {session['email']}")
    else:
        flash(f"You are not logged in")
    return render_template('home.html', posts=Post.query.order_by(Post.id.desc()).all())    # reverse order


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
    if form.validate_on_submit() and user.query.filter_by(username=form.username.data).first() == None and user.query.filter_by(email=form.email.data).first() == None:
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        if request.cookies.get('email') == None or bool(request.cookies.get('remember')) == False:
            print("entered here", bool(request.cookies.get('remember')))
            form = LoginForm()
        else:
            print("entered there", bool(request.cookies.get('remember')))
            form = LoginForm(email=request.cookies.get('email'))
    except Exception as e:
        print(f'Exception 2' + str(e))

    try:
        if session['email'] == "admin@blog.com":
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('home'))
    except Exception as e:
        print(f'Exception 3' + str(e))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password == form.password.data:
            email = request.form['email']
            session['email'] = email
            password = request.form['password']
            session['password'] = password

            if form.remember.data:
                print("enter this area")
                remember = request.form['remember']
                session['remember'] = remember


            if form.email.data == 'admin@blog.com':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    form = Logout()
    if form.is_submitted():
        #if remember me is check need to move sessions to long term cookies
        try:
            resp = make_response(redirect(url_for('login')))
            if bool(session.get('remember')) == True:
                email = request.cookies.get('email',session.get('email'))
                #resp = make_response('login.html', render_template('login.html', title='Login', form=LoginForm(email=email, password=password, remember=bool(session.get('remember')))))
                resp.set_cookie('email', session.get('email'))#errorline
                resp.set_cookie('remember', session['remember'])
                clear_session()
                return resp
        except Exception as e:
            print(f'Exception 1 {e}')
        
        if request.cookies.get('email') == session.get('email'):
            delete_cookie(resp)
        clear_session()
        return resp
    return render_template('logout.html', form=form)


def clear_session():
    session.clear()    
    for x in session:
        x=None


def delete_cookie(resp):
    resp.set_cookie('remember','', max_age=0)
    resp.set_cookie('email','', max_age=0)
    return resp


@app.route('/user/picture', methods=['GET'])
def user_picture():
    # allows caching of picture for better performance
    user = db.session.query(User).filter_by(email=session['email']).first()
    if user.image is None:
        with open("static/default.jpg", "rb") as file:
            image = bytearray(file.read())
    else:
        image = user.image
    return app.response_class(image, mimetype='application/octet-stream')


@app.route("/photo", methods=['GET', 'POST'])
def photo():
    session_email = session.get('email')
    if session_email is None or session_email == "":
        flash(f'You need to log in to view or post photo', 'warning')
        return redirect(url_for('login'))
    # to allow file upload need following in form html: enctype = "multipart/form-data"
    form = PhotoForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = db.session.query(User).filter_by(email=session['email']).first()
        user.image_file = form.photo.name
        f = form.photo.data
        user.image = f.read()
        db.session.commit()
        flash(f'Photo uploaded', 'success')
        return redirect(url_for('photo'))
    # flash(f'Photo failed', 'error')
    return render_template('photo.html', title='Photo', form=form)


@app.route("/comment", methods=['GET', 'POST'])
def comment():
    form = CommentForm()
    session_email = session.get('email')
    if session_email is None or session_email == "":
        flash(f'You need to log in to comment', 'warning')
        return redirect(url_for('login'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=session['email']).first()
        post = Post(title=form.title.data, content=form.text.data, user_id=user.id)
        db.session.add(post)
        db.session.commit()
        flash(f'Post created', 'success')
        return redirect(url_for('home'))
    return render_template('comment.html', title='Comment', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    