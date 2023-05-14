#!/usr/bin/python3
"""
This module contains the several unit tests for the 'Amenity' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
Amenity = __import__('models.amenity').amenity.Amenity
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestAmenity(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'Place'
    class
    """

    def test_amenity_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertTrue(hasattr(amenity1, "id"))
        self.assertTrue(hasattr(amenity2, "id"))
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertIsInstance(amenity1.id, str)
        self.assertIsInstance(amenity2.id, str)

    def test_amenity_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        amenity_test = Amenity()
        self.assertTrue(hasattr(amenity_test, "id"))
        self.assertTrue(hasattr(amenity_test, "created_at"))
        self.assertTrue(hasattr(amenity_test, "updated_at"))
        self.assertTrue(hasattr(amenity_test, "name"))
        self.assertTrue(hasattr(amenity_test, "save"))
        self.assertTrue(hasattr(amenity_test, "to_dict"))

    def test_amenity_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        amenity_test = Amenity()
        self.assertEqual(amenity_test.name, "")

    def test_amenity_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        amenity_test = Amenity()
        self.assertIsInstance(amenity_test.id, str)
        self.assertIsInstance(amenity_test.created_at, datetime)
        self.assertIsInstance(amenity_test.updated_at, datetime)
        self.assertIsInstance(amenity_test.name, str)

    def test_amenity_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        amenity_test = Amenity()
        self.assertTrue(issubclass(type(amenity_test), BaseModel))

    def test_amenity_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        amenity_test = Amenity()
        display = "[{:s}] ({:s}) {}\n".format(
                type(amenity_test).__name__, amenity_test.id,
                amenity_test.__dict__)
        print(amenity_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_amenity_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        amenity_test = Amenity()
        self.assertEqual(amenity_test.created_at,
                         amenity_test.updated_at)
        amenity_test.save()
        self.assertNotEqual(amenity_test.created_at,
                            amenity_test.updated_at)

    def test_amenity_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        amenity_test = Amenity()
        self.assertTrue(hasattr(amenity_test, "id"))
        self.assertTrue(hasattr(amenity_test, "created_at"))
        self.assertTrue(hasattr(amenity_test, "updated_at"))
        self.assertTrue(hasattr(amenity_test, "name"))
        self.assertFalse(hasattr(amenity_test, "email"))
        self.assertFalse(hasattr(amenity_test, "password"))
        self.assertFalse(hasattr(amenity_test, "first_name"))
        self.assertFalse(hasattr(amenity_test, "last_name"))

    def test_amenity_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        amenity_test = Amenity(*args)
        self.assertTrue(hasattr(amenity_test, "id"))
        self.assertTrue(hasattr(amenity_test, "created_at"))
        self.assertTrue(hasattr(amenity_test, "updated_at"))
        self.assertTrue(hasattr(amenity_test, "name"))
        self.assertFalse(hasattr(amenity_test, "email"))
        self.assertFalse(hasattr(amenity_test, "password"))
        self.assertFalse(hasattr(amenity_test, "first_name"))
        self.assertFalse(hasattr(amenity_test, "last_name"))
        self.assertFalse(hasattr(amenity_test, "age"))

    def test_amenity_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        amenity_test = Amenity(*args, **dictionary)
        dictionary = amenity_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertTrue("email" not in dictionary)
        self.assertTrue("password" not in dictionary)
        self.assertTrue("first_name" not in dictionary)
        self.assertTrue("last_name" not in dictionary)
        self.assertTrue("name" in dictionary)

        dictionary["name"] = "Iris"

        amenity_test = Amenity(**dictionary)
        self.assertEqual(amenity_test.id, dictionary["id"])
        self.assertEqual(amenity_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(amenity_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(amenity_test.name, dictionary["name"])

        self.assertIsInstance(amenity_test, Amenity)
        self.assertIsInstance(amenity_test.created_at, datetime)
        self.assertIsInstance(amenity_test.updated_at, datetime)
        self.assertIsInstance(amenity_test.name, str)
