from flask_sqlalchemy import SQLAlchemy

from flask_weekend_mini_project.db_interface import User, Post, db
from flask_weekend_mini_project.flaskblog import app, config_for_production

test_user_name = 'test'
test_user_email = 'test@gmail.com'
test_user_password = '123'

def config_for_test(target_app, target_db):
    target_app.config['SECRET_KEY'] = 'gobblywobbly'
    target_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    target_app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024  # limit size of uploads
    target_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    target_db.init_app(app)
    with app.app_context():
        db.create_all()
        test_user = User(username=test_user_name, email=test_user_email, password=test_user_password)
        db.session.add(test_user)
        db.session.commit()
        user = User.query.filter_by(username=test_user_name).first()
        post = Post(title='how to have fun', content='Some text')
        user.posts.append(post)
        db.session.add(post)
        db.session.commit()


config_for_test(app, db)


def test_home_page_get():
    app.config.from_mapping({'TESTING': True})
    assert app.testing
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert all(x in response.data for x in [b'Flask Blog', b'Home'])


def test_comment_page_not_logged_in():
    app.config.from_mapping({'TESTING': True})
    assert app.testing
    with app.test_client() as test_client:
        response = test_client.get('/comment', follow_redirects=True)
        # https://flask.palletsprojects.com/en/2.0.x/testing/  Following redirects
        assert len(response.history) == 1
        assert response.request.path == "/login"


def test_login_page():
    app.config.from_mapping({'TESTING': True, 'WTF_CSRF_ENABLED': False})
    assert app.testing
    with app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        assert all(x in response.data for x in [b'Log In', b'Email', b'Password'])
        test_client.post('/login', data={'email': test_user_email, 'password': test_user_password})
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.request.path == "/"
        assert all(x in response.data for x in [b'Logged in', b'Welcome', bytes(test_user_email,'utf-8')])
