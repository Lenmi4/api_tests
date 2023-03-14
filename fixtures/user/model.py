import attr
from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


# class CreateUser(BaseClass):
#     def __init__(self, id, username, firstname, lastname, email, password, phone, user_status):
#         self.id = id
#         self.username = username
#         self.firstName = firstname
#         self.lastName = lastname
#         self.email = email
#         self.password = password
#         self.phone = phone
#         self.userStatus = user_status
#
#     @staticmethod
#     def random():
#         return CreateUser(id=0,
#                           username="string",
#                           firstname="string",
#                           lastname="string",
#                           email=fake.email(),
#                           password=fake.password(),
#                           phone="string",
#                           user_status=0)


@attr.s
class CreateUser(BaseClass):
    id: int = attr.ib(default=None)
    username: str = attr.ib(default=None)
    firstname: str = attr.ib(default=None)
    lastname: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    password: str = attr.ib(default=None)
    phone: str = attr.ib(default=None)
    user_status: int = attr.ib(default=None)

    @staticmethod
    def random():
        return CreateUser(id=0,
                          username="string",
                          firstname="string",
                          lastname="string",
                          email=fake.email(),
                          password=fake.password(),
                          phone="string",
                          user_status=0)


# class LoginUser(BaseClass):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     @staticmethod
#     def random():
#         return LoginUser(username=fake.email(), password=fake.password())

@attr.s
class LoginUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return LoginUser(username=fake.email(), password=fake.password())


@attr.s
class GetUsername(BaseClass):
    username: str = attr.ib(default=None)

    @staticmethod
    def random():
        return GetUsername(username=fake.email())
