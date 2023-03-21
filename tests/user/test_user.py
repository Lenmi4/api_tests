from fixtures.user.model import LoginUser, CreateUser, GetUsername


class TestAuth:
    def test_create_user(self, app, create):
        assert create.status_code == 200

    def test_user_login_valid_data(self, app, login):
        assert login.status_code == 200

    # def test_user_login_random_data(self, app, login):
    #     assert login.status_code == 200

    def test_user_logout(self, app, login, logout):
        assert logout.status_code == 200

    def test_get_username(self, app, create):
        assert create.status_code == 200
        res = app.user.get_username(data=create.username)
        assert res.status_code == 200


