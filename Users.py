from jsonschema._validators import items


class users():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
