import json

from fixtures.user.model import LoginUser, CreateUser, GetUsername


class TestAuth:
    def test_create_user(self, app, create):
        assert create.status_code == 200

    def test_user_login_valid_data(self, app, login):
        assert login.status_code == 200

    # def test_user_login_not_create_user(self, login_not_create):
    #     assert login_not_create.status_code == 400

    def test_user_logout(self, app, login, logout):
        assert logout.status_code == 200

    def test_get_user(self, app, create):
        assert create.status_code == 200
        res1 = app.user.get_user("string")
        assert res1.status_code == 200

    def test_put_user(self, app, create):
        assert create.status_code == 200
        res1 = app.user.put_user()
        assert res1.status_code == 200

    def test_delete_user(self, app, create):
        assert create.status_code == 200
        res1 = app.user.delete_user("string")
        assert res1.status_code == 200
