#!/usr/bin/python3
"""
This module contains the definition for the 'Place' class which is a subclass
of the 'BaseModel' class
"""


from .base_model import BaseModel


class Place(BaseModel):
    """
    A class representation of a place with several attributes to capture
    information about the plae such as:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be the list
        of Amenity.id later
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs is None or len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []
        else:
            if "city_id" in kwargs:
                self.city_id = kwargs["city_id"]
            else:
                self.city_id = ""
            if "user_id" in kwargs:
                self.user_id = kwargs["user_id"]
            else:
                self.user_id = ""
            if "name" in kwargs:
                self.name = kwargs["name"]
            else:
                self.name = ""
            if "description" in kwargs:
                self.description = kwargs["description"]
            else:
                self.description = ""
            if "number_rooms" in kwargs:
                self.number_rooms = kwargs["number_rooms"]
            else:
                self.number_rooms = 0
            if "number_bathrooms" in kwargs:
                self.number_bathrooms = kwargs["number_bathrooms"]
            else:
                self.number_bathrooms = 0
            if "max_guest" in kwargs:
                self.max_guest = kwargs["max_guest"]
            else:
                self.max_guest = 0
            if "price_by_night" in kwargs:
                self.price_by_night = kwargs["price_by_night"]
            else:
                self.price_by_night = 0
            if "latitude" in kwargs:
                self.latitude = kwargs["latitude"]
            else:
                self.latitude = 0.0
            if "longitude" in kwargs:
                self.longitude = kwargs["longitude"]
            else:
                self.longitude = 0.0
            if "amenity_ids" in kwargs:
                self.amenity_ids = kwargs["amenity_ids"]
            else:
                self.amenity_ids = []
