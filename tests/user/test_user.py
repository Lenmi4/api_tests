import pytest

from conftest import fake
from fixtures.user.model import LoginUser, CreateUser


class TestAuth:
    def test_create_user(self, app):
        data = CreateUser.random()
        res = app.user.create_user(data)
        assert res.status_code == 200

    def test_user_login_valid_data(self, app):
        data = LoginUser.random()
        res = app.user.login_user(data)
        assert res.status_code == 200

    # def test_user_login_invalid_data(self, app):
    #     data = {"username": fake.email(), "password": fake.password()}
    #     res = app.user.login_user(data)
    #     assert res.status_code == 400
