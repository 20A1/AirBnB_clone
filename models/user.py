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
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
        else:
            if "email" in kwargs:
                self.email = kwargs["email"]
            else:
                self.email = ""
            if "password" in kwargs:
                self.password = kwargs["password"]
            else:
                self.password = ""
            if "first_name" in kwargs:
                self.first_name = kwargs["email"]
            else:
                self.first_name = ""
            if "last_name" in kwargs:
                self.last_name = kwargs["last_name"]
            else:
                self.last_name = ""
