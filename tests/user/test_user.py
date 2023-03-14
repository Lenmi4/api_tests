
from fixtures.user.model import LoginUser, CreateUser, GetUsername


class TestAuth:
    def test_create_user(self, app, auth):
        # data = CreateUser.random()
        # res = app.user.create_user(data)
        assert auth.status_code == 200
        #assert res.json().get('message') == UserText.MESSAGE_CREATE_USER, 'Some words'

    def test_user_login_valid_data(self, app):
        data = LoginUser.random()
        res = app.user.login_user(data)
        assert res.status_code == 200

    def test_user_logout(self, app):
        res = app.user.logout_user()
        assert res.status_code == 200

    def test_get_username(self, app):
        data = CreateUser.random()
        res = app.user.create_user(data)
        assert res.status_code == 200
        res = app.user.get_username(data=data.username)


