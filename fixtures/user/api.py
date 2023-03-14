from requests import Response

from fixtures.user.model import CreateUser, LoginUser, GetUsername


class User:
    def __init__(self, app):
        self.app = app

    CREATE_USER = "/user"
    LOGIN_USER = "/user/login"
    LOGOUT_USER = "/user/logout"
    GET_USER_BY_USERNAME = "/user/{username}"
    UPDATED_USER = "/user/{username}"
    DELETE_USER = "/user/{username}"

    def create_user(self, data: CreateUser) -> Response:
        """
        https://petstore.swagger.io/#/user/createUser
        """
        res = self.app.client.request(method='POST',
                                      url=f"{self.app.url}{self.CREATE_USER}",
                                      json=data.to_dict())
        return res

    def login_user(self, data: LoginUser) -> Response:
        """
        https://petstore.swagger.io/#/user/loginUser
        """
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.LOGIN_USER}",
                                      json=data.to_dict())
        return res

    def logout_user(self) -> Response:
        """
        https://petstore.swagger.io/#/user/logoutUser
        """
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.LOGOUT_USER}"
                                      )
        return res

    def get_username(self, data: GetUsername) -> Response:
        """
        https://petstore.swagger.io/#/user/getUserByName
        """
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.GET_USER_BY_USERNAME}",
                                      json=data.to_dict())
        return res
