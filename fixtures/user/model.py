from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


class CreateUser(BaseClass):
    def __init__(self, id, username, firstname, lastname, email, password, phone, user_status):
        self.id = id
        self.username = username
        self.firstName = firstname
        self.lastName = lastname
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = user_status

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


class LoginUser(BaseClass):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        return LoginUser(username=fake.email(), password=fake.password())

