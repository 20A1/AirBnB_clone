#!/usr/bin/python3
"""
This module contains the several unit tests for the 'City' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
City = __import__('models.city').city.City
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestCity(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'Place'
    class
    """

    def test_city_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        city1 = City()
        city2 = City()
        self.assertTrue(hasattr(city1, "id"))
        self.assertTrue(hasattr(city2, "id"))
        self.assertNotEqual(city1.id, city2.id)
        self.assertIsInstance(city1.id, str)
        self.assertIsInstance(city2.id, str)

    def test_city_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        city_test = City()
        self.assertTrue(hasattr(city_test, "id"))
        self.assertTrue(hasattr(city_test, "created_at"))
        self.assertTrue(hasattr(city_test, "updated_at"))
        self.assertTrue(hasattr(city_test, "name"))
        self.assertTrue(hasattr(city_test, "state_id"))
        self.assertTrue(hasattr(city_test, "save"))
        self.assertTrue(hasattr(city_test, "to_dict"))

    def test_city_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        city_test = City()
        self.assertEqual(city_test.name, "")
        self.assertEqual(city_test.state_id, "")

    def test_city_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        city_test = City()
        self.assertIsInstance(city_test.id, str)
        self.assertIsInstance(city_test.created_at, datetime)
        self.assertIsInstance(city_test.updated_at, datetime)
        self.assertIsInstance(city_test.name, str)
        self.assertIsInstance(city_test.state_id, str)

    def test_city_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        city_test = City()
        self.assertTrue(issubclass(type(city_test), BaseModel))

    def test_city_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        city_test = City()
        display = "[{:s}] ({:s}) {}\n".format(
                type(city_test).__name__, city_test.id,
                city_test.__dict__)
        print(city_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_city_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        city_test = City()
        self.assertEqual(city_test.created_at,
                         city_test.updated_at)
        city_test.save()
        self.assertNotEqual(city_test.created_at,
                            city_test.updated_at)

    def test_city_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        city_test = City()
        self.assertTrue(hasattr(city_test, "id"))
        self.assertTrue(hasattr(city_test, "created_at"))
        self.assertTrue(hasattr(city_test, "updated_at"))
        self.assertTrue(hasattr(city_test, "name"))
        self.assertTrue(hasattr(city_test, "state_id"))
        self.assertFalse(hasattr(city_test, "email"))
        self.assertFalse(hasattr(city_test, "password"))
        self.assertFalse(hasattr(city_test, "first_name"))
        self.assertFalse(hasattr(city_test, "last_name"))

    def test_city_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        city_test = City(*args)
        self.assertTrue(hasattr(city_test, "id"))
        self.assertTrue(hasattr(city_test, "created_at"))
        self.assertTrue(hasattr(city_test, "updated_at"))
        self.assertTrue(hasattr(city_test, "name"))
        self.assertTrue(hasattr(city_test, "state_id"))
        self.assertFalse(hasattr(city_test, "email"))
        self.assertFalse(hasattr(city_test, "password"))
        self.assertFalse(hasattr(city_test, "first_name"))
        self.assertFalse(hasattr(city_test, "last_name"))
        self.assertFalse(hasattr(city_test, "age"))

    def test_city_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        city_test = City(*args, **dictionary)
        dictionary = city_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertFalse("email" in dictionary)
        self.assertFalse("password" in dictionary)
        self.assertFalse("first_name" in dictionary)
        self.assertFalse("last_name" in dictionary)
        self.assertTrue("name" in dictionary)
        self.assertTrue("state_id" in dictionary)

        dictionary["name"] = "Iris"
        dictionary["state_id"] = "1234-1234-1234-1234"

        city_test = City(**dictionary)
        self.assertEqual(city_test.id, dictionary["id"])
        self.assertEqual(city_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(city_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(city_test.name, dictionary["name"])
        self.assertEqual(city_test.state_id, dictionary["state_id"])

        self.assertIsInstance(city_test, City)
        self.assertIsInstance(city_test.id, str)
        self.assertIsInstance(city_test.created_at, datetime)
        self.assertIsInstance(city_test.updated_at, datetime)
        self.assertIsInstance(city_test.name, str)
        self.assertIsInstance(city_test.state_id, str)
