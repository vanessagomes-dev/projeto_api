# models/user.py  modelo para registrar novos usuarios

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
