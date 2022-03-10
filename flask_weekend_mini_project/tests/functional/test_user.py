from flaskblog import create_app,Config


def test_home_page():

    flask_app = create_app(Config)

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 405
        assert b'Flask User Managment Example!' not in response.data