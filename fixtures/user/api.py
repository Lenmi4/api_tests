
from requests import Response

from common.decorator import logger as log
from fixtures.user.model import CreateUser, LoginUser, GetUsername


class User:
    def __init__(self, app):
        self.app = app

    CREATE_USER = "/user"
    LOGIN_USER = "/user/login"
    LOGOUT_USER = "/user/logout"
    GET_USER_BY_USERNAME = "/user/{}"
    PUT_USER = "/user/{}"
    DELETE_USER = "/user/{}"

    #@log("Create new user")
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

    # def login_not_create_user(self, data: LoginUser) -> Response:
    #     """
    #     https://petstore.swagger.io/#/user/loginUser
    #     """
    #     res = self.app.client.request(method='GET',
    #                                   url=f"{self.app.url}{self.LOGIN_USER}",
    #                                   json=data.to_dict())
    #     return res

    def logout_user(self) -> Response:
        """
        https://petstore.swagger.io/#/user/logoutUser
        """
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.LOGOUT_USER}")
        return res

    def get_user(self, username) -> Response:
        """
        https://petstore.swagger.io/#/user/getUserByName
        """
        res = self.app.client.request(method='GET',
                                      url=f"{self.app.url}{self.GET_USER_BY_USERNAME.format(username)}")
        return res

    def put_user(self, username) -> Response:
        """
        https://petstore.swagger.io/#/user/updateUser
        """
        res = self.app.client.request(method='PUT',
                                      url=f"{self.app.url}{self.PUT_USER.format(username)}")
        return res

    def delete_user(self, username) -> Response:
        """
        https://petstore.swagger.io/#/user/deleteUser
        """
        res = self.app.client.request(method='DELETE',
                                      url=f"{self.app.url}{self.DELETE_USER.format(username)}")
        return res

