from flask_weekend_mini_project.flaskblog import app
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
    app.config.from_mapping({'TESTING': True})
    assert app.testing
    with app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        assert all(x in response.data for x in [b'Log In', b'Email', b'Password'])
        test_client.post('login', data=dict(email='george@gmail.com', password='123'))
        assert response.status_code == 200
        assert response.request.path == "/"