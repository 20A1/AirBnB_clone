#!/usr/bin/python3
"""
This Module contains the definition for the 'User' class which is a subclass of
the 'BaseModel' class and a data structure to represent users.
"""


from .base_model import BaseModel


class User(BaseModel):
    """
    A class representation of a user and a subclass of the 'BaseModel' class

    It captures the information of the users in its atttributes which include:
        - email
        - password
        - first_name
        - last_name
    """

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if kwargs is not None and len(kwargs) > 0:
            for key in kwargs:
                if key == "__class__":
                    continue
                setattr(self, key, kwargs[key])
        super().__init__(*args, **kwargs)
