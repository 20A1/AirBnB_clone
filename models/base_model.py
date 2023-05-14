#!/usr/bin/python3
"""
This module contains the definition for the BaseModel class that defines all
common attributes/methods for other classes
"""


import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    This class will serve as the base class for other classes to be implemented
    Attributes in this class are:
        - Public instance attributes:
            * id: string - assign with an uuid when an instance is created
            * created_at: datetime - assign with the current datetime when an
            instance is created
            * updated_at: datetime - assign with the current datetime when an
            instance is created and it will be updated everytime you change
            your object
        - Public instance method:
            * save(self): updates the 'updated_at' attr with the current
            datetime
            * to_dict(self): returns a dictionary containing all keys/values of
            '__dict__' of the instance
    """

    def __init__(self, *args, **kwargs):
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """
        Return a string representation of the class
        """
        return ("[{0:s}] ({1:s}) {2:}".format(type(self).__name__, self.id,
                                              self.__dict__))

    def save(self):
        """
        Update the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of '__dict__' of the
        instance
        """
        curr = self.__dict__.copy()
        curr["__class__"] = type(self).__name__
        curr["created_at"] = "{:%Y-%m-%dT%H:%M:%S.%f}".format(self.created_at)
        curr["updated_at"] = "{:%Y-%m-%dT%H:%M:%S.%f}".format(self.updated_at)
        return (curr)
