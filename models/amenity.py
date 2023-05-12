#!/usr/bin/python3
"""
This module contains the class definition for 'Amenity' which is a subclass of
the 'BaseModel' class
"""


from .base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representation of the amenities of the place with the only
    attribute being the name of the amenity
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) == 0:
            self.name = ""
        else:
            if "name" in kwargs:
                self.name = kwargs["name"]
            else:
                self.name = ""

