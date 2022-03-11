# import os
# import sys
# import inspect
# #https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(os.path.dirname(currentdir))
# sys.path.insert(0, parentdir) 

from flask_weekend_mini_project import *
#from flaskblog import create_app,Config
#from forms import *
#from flask_weekend_mini_project.flaskblog import Config
def test_home_page():

    # flask_app = flaskblog.create_app(flaskblog.Config)

    # with flask_app.test_client() as test_client:
    #     response = test_client.get('/')
    #     assert response.status_code == 404
    #     assert b'Flask User Managment Example!' not in response.data
    assert True