import pytest

from conftest import fake


class TestAuth:
    def test_user_valid_data(self, app):

        data = {"username": fake.email(), "password": fake.password()}
        res = app.user.create_user(data)
        assert res.status_code == 201
