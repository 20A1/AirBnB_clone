#!/usr/bin/python3
"""
This module contains the definition for the 'City' class which is a subclass of
the 'BaseModel' class
"""


from .base_model import BaseModel


class City(BaseModel):
    """
    A class representation of a city, with attributes as follows:

        - state_id: string - empty string: it will be the State.id
        - name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.state_id = ""
            self.name = ""
        else:
            if "state_id" in kwargs:
                self.state_id = kwargs["state_id"]
            else:
                self.state_id = ""
            if "name" in kwargs:
                self.name = kwargs["name"]
            else:
                self.name = ""
        super().__init__(*args, **kwargs)
