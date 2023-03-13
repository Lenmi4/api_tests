from requests import Response

from fixtures.user.model import CreateUser, LoginUser


class User:
    def __init__(self, app):
        self.app = app

    CREATE_USER = "/user"
    LOGIN_USER = "/user/login"

    def create_user(self, data: CreateUser) -> Response:
        """
        https://petstore.swagger.io/#/user/createUser
        """
        res = self.app.client.request(method='POST',
                                      url=f"{self.app.url}{self.CREATE_USER}",
                                      json=data.to_dict())
        return res

    def login_user(self, data: LoginUser) -> Response:
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.LOGIN_USER}",
                                      json=data.to_dict())
        return res
