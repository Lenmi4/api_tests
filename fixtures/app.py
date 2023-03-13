from fixtures.request import Client
from fixtures.user.api import User


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.user = User(self)
