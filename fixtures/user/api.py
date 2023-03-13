import json

from requests import Response


def to_dict(self):
    return json.loads(json.dumps(self, default=lambda o: o.__dict__))


class User:
    def __init__(self, app):
        self.app = app

    CREATE_USER = "/user"
    LOGIN_USER = "/user/login"

    def create_user(self, data: dict) -> Response:
        res = self.app.client.request(method='POST',
                                      url=f"{self.app.url}{self.CREATE_USER}",
                                      json=to_dict(data))
        return res

    def login_user(self, data: dict) -> Response:
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.LOGIN_USER}",
                                      json=to_dict(data))
        return res
