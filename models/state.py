#!/usr/bin/python3
"""
A module containing the definition for the 'State' class which is a subclass of
the 'BaseModel' class
"""


from .base_model import BaseModel


class State(BaseModel):
    """
    A class representation of a state, this class inherits from the 'BaseModel'
    class and has one additional class attribute 'name'
    """

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.name = ""
        else:
            if "name" in kwargs:
                self.name = kwargs["name"]
        super().__init__(*args, **kwargs)
