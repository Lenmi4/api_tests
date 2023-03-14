import cattr
from requests import Response

from fixtures.user.api import User


class Validator:
    def structure(self, response: User, type_response) -> User:
        if type_response:
            try:
                response.data = cattr.structure(response.json(), type_response)
            except Exception as e:
                raise e
        return response
