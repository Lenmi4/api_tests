from fixtures.user.api import User


class Client:
    def __init__(self, url):
        self.url = url
        self.user = User(self)
