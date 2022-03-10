import flaskblog

#test functions should start with the word test
def test_new_user():
    """
    Tests the User model for when a new user is defined that the values are correctly defined    
    """
    user = flaskblog.User(username='user', email='other@example.com',password='12334')
    assert user.username == 'user'
    assert user.email == 'other@example.com'
    assert user.password == '12334'
