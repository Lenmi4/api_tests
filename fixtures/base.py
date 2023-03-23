import json


class BaseClass:
    def to_dict(self) -> dict:
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
