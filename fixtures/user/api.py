import requests
from requests import Response


class User:
    def __init__(self, client):
        self.client = client

    POST_USER = "/user"

    def create_user(self, data: dict) -> Response:
        res = requests.post(url=f"{self.client.url}{self.POST_USER}", json=data)
        return res
