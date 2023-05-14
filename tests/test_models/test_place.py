#!/usr/bin/python3
"""
This module contains the several unit tests for the 'Place' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
Place = __import__('models.place').place.Place
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestPlace(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'Place'
    class
    """

    def test_place_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        place1 = Place()
        place2 = Place()
        self.assertTrue(hasattr(place1, "id"))
        self.assertTrue(hasattr(place2, "id"))
        self.assertNotEqual(place1.id, place2.id)
        self.assertIsInstance(place1.id, str)

    def test_place_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        place_test = Place()
        self.assertTrue(hasattr(place_test, "created_at"))
        self.assertTrue(hasattr(place_test, "updated_at"))
        self.assertTrue(hasattr(place_test, "city_id"))
        self.assertTrue(hasattr(place_test, "user_id"))
        self.assertTrue(hasattr(place_test, "name"))
        self.assertTrue(hasattr(place_test, "description"))
        self.assertTrue(hasattr(place_test, "number_rooms"))
        self.assertTrue(hasattr(place_test, "number_bathrooms"))
        self.assertTrue(hasattr(place_test, "max_guest"))
        self.assertTrue(hasattr(place_test, "price_by_night"))
        self.assertTrue(hasattr(place_test, "latitude"))
        self.assertTrue(hasattr(place_test, "longitude"))
        self.assertTrue(hasattr(place_test, "amenity_ids"))
        self.assertTrue(hasattr(place_test, "save"))
        self.assertTrue(hasattr(place_test, "to_dict"))

    def test_place_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        place_test = Place()
        self.assertEqual(place_test.city_id, "")
        self.assertEqual(place_test.user_id, "")
        self.assertEqual(place_test.name, "")
        self.assertEqual(place_test.description, "")
        self.assertEqual(place_test.number_rooms, 0)
        self.assertEqual(place_test.number_bathrooms, 0)
        self.assertEqual(place_test.max_guest, 0)
        self.assertEqual(place_test.price_by_night, 0)
        self.assertEqual(place_test.latitude, 0.0)
        self.assertEqual(place_test.longitude, 0.0)
        self.assertEqual(place_test.amenity_ids, [])

    def test_place_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        place_test = Place()
        self.assertIsInstance(place_test.created_at, datetime)
        self.assertIsInstance(place_test.updated_at, datetime)
        self.assertIsInstance(place_test.city_id, str)
        self.assertIsInstance(place_test.user_id, str)
        self.assertIsInstance(place_test.name, str)
        self.assertIsInstance(place_test.description, str)
        self.assertIsInstance(place_test.number_rooms, int)
        self.assertIsInstance(place_test.number_bathrooms, int)
        self.assertIsInstance(place_test.max_guest, int)
        self.assertIsInstance(place_test.price_by_night, int)
        self.assertIsInstance(place_test.latitude, float)
        self.assertIsInstance(place_test.longitude, float)
        self.assertIsInstance(place_test.amenity_ids, list)

    def test_place_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        place_test = Place()
        self.assertTrue(issubclass(type(place_test), BaseModel))

    def test_place_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        place_test = Place()
        display = "[{:s}] ({:s}) {}\n".format(
                type(place_test).__name__, place_test.id,
                place_test.__dict__)
        print(place_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_place_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        place_test = Place()
        self.assertEqual(place_test.created_at,
                         place_test.updated_at)
        place_test.save()
        self.assertNotEqual(place_test.created_at,
                            place_test.updated_at)

    def test_place_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        place_test = Place()
        self.assertTrue(hasattr(place_test, "id"))
        self.assertTrue(hasattr(place_test, "created_at"))
        self.assertTrue(hasattr(place_test, "updated_at"))
        self.assertTrue(hasattr(place_test, "city_id"))
        self.assertTrue(hasattr(place_test, "user_id"))
        self.assertTrue(hasattr(place_test, "name"))
        self.assertTrue(hasattr(place_test, "description"))
        self.assertTrue(hasattr(place_test, "number_rooms"))
        self.assertTrue(hasattr(place_test, "number_bathrooms"))
        self.assertTrue(hasattr(place_test, "max_guest"))
        self.assertTrue(hasattr(place_test, "price_by_night"))
        self.assertTrue(hasattr(place_test, "latitude"))
        self.assertTrue(hasattr(place_test, "longitude"))
        self.assertTrue(hasattr(place_test, "amenity_ids"))

    def test_place_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        place_test = Place(*args)
        self.assertTrue(hasattr(place_test, "id"))
        self.assertTrue(hasattr(place_test, "created_at"))
        self.assertTrue(hasattr(place_test, "updated_at"))
        self.assertTrue(hasattr(place_test, "city_id"))
        self.assertTrue(hasattr(place_test, "user_id"))
        self.assertTrue(hasattr(place_test, "name"))
        self.assertTrue(hasattr(place_test, "description"))
        self.assertTrue(hasattr(place_test, "number_rooms"))
        self.assertTrue(hasattr(place_test, "number_bathrooms"))
        self.assertTrue(hasattr(place_test, "max_guest"))
        self.assertTrue(hasattr(place_test, "price_by_night"))
        self.assertTrue(hasattr(place_test, "latitude"))
        self.assertTrue(hasattr(place_test, "longitude"))
        self.assertTrue(hasattr(place_test, "amenity_ids"))

    def test_place_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        place_test = Place(*args, **dictionary)
        dictionary = place_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertTrue("city_id" in dictionary)
        self.assertTrue("user_id" in dictionary)
        self.assertTrue("name" in dictionary)
        self.assertTrue("description" in dictionary)
        self.assertTrue("number_rooms" in dictionary)
        self.assertTrue("number_bathrooms" in dictionary)
        self.assertTrue("max_guest" in dictionary)
        self.assertTrue("price_by_night" in dictionary)
        self.assertTrue("latitude" in dictionary)
        self.assertTrue("longitude" in dictionary)
        self.assertTrue("amenity_ids" in dictionary)

        dictionary["city_id"] = "1212-1212-1212-1212"
        dictionary["user_id"] = "1234-1234-1234-1234"
        dictionary["name"] = "Iris"
        dictionary["description"] = "Room in a condo hosted by Valentina"
        dictionary["number_rooms"] = 1
        dictionary["number_bathrooms"] = 2
        dictionary["max_guest"] = 5
        dictionary["price_by_night"] = 122
        dictionary["latitude"] = 23.4721
        dictionary["longitude"] = 67.87419
        dictionary["amenity_ids"] = ["1122-3344-5566-7788",
                                     "1324-5768-9012-4365"]

        place_test = Place(**dictionary)
        self.assertEqual(place_test.id, dictionary["id"])
        self.assertEqual(place_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(place_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(place_test.city_id, dictionary["city_id"])
        self.assertEqual(place_test.user_id, dictionary["user_id"])
        self.assertEqual(place_test.name, dictionary["name"])
        self.assertEqual(place_test.description, dictionary["description"])
        self.assertEqual(place_test.number_rooms, dictionary["number_rooms"])
        self.assertEqual(place_test.number_bathrooms,
                         dictionary["number_bathrooms"])
        self.assertEqual(place_test.max_guest, dictionary["max_guest"])
        self.assertEqual(place_test.price_by_night,
                         dictionary["price_by_night"])
        self.assertEqual(place_test.latitude, dictionary["latitude"])
        self.assertEqual(place_test.longitude, dictionary["longitude"])
        self.assertEqual(place_test.amenity_ids, dictionary["amenity_ids"])

        self.assertIsInstance(place_test, Place)
        self.assertIsInstance(place_test.created_at, datetime)
        self.assertIsInstance(place_test.updated_at, datetime)
        self.assertIsInstance(place_test.city_id, str)
        self.assertIsInstance(place_test.user_id, str)
        self.assertIsInstance(place_test.name, str)
        self.assertIsInstance(place_test.description, str)
        self.assertIsInstance(place_test.number_rooms, int)
        self.assertIsInstance(place_test.number_bathrooms, int)
        self.assertIsInstance(place_test.max_guest, int)
        self.assertIsInstance(place_test.price_by_night, int)
        self.assertIsInstance(place_test.latitude, float)
        self.assertIsInstance(place_test.longitude, float)
        self.assertIsInstance(place_test.amenity_ids, list)
