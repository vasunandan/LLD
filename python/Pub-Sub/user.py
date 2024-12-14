from abc import ABC
from pydantic import BaseModel

class User():
    _counter = 0
    def __new__(cls):
        if _counter == 0:
            return super().__init__(cls)
        else:
            print("INstance already exists")

    def __init__(username:str,email:str):
        User._counter += 1
        self.user_id = User._counter
        self.username = username
        self.email = email
        self.id = 