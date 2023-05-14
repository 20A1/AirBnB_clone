#!/usr/bin/python3
"""
This module contains the class definition for the 'Reveiw' class which is a
subclass for the 'BaseModel' class
"""


from .base_model import BaseModel


class Review(BaseModel):
    """
    A class representation for a user's review, with attributes to capture the
    information such as:

        - place_id: string - empty string: it will be the Place.id
        - user_id: string - empty string: it will be the User.id
        - text: string - empty string
    """

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
        else:
            for key in kwargs:
                if key == "__class__":
                    continue
                setattr(self, key, kwargs[key])
        super().__init__(*args, **kwargs)
