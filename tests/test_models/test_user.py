#!/usr/bin/python3
"""
This module contains the several unit tests for the 'User' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
User = __import__('models.user').user.User
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestUser(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'Place'
    class
    """

    def test_user_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        user1 = User()
        user2 = User()
        self.assertTrue(hasattr(user1, "id"))
        self.assertTrue(hasattr(user2, "id"))
        self.assertNotEqual(user1.id, user2.id)
        self.assertIsInstance(user1.id, str)
        self.assertIsInstance(user2.id, str)

    def test_user_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        user_test = User()
        self.assertTrue(hasattr(user_test, "id"))
        self.assertTrue(hasattr(user_test, "created_at"))
        self.assertTrue(hasattr(user_test, "updated_at"))
        self.assertTrue(hasattr(user_test, "email"))
        self.assertTrue(hasattr(user_test, "password"))
        self.assertTrue(hasattr(user_test, "first_name"))
        self.assertTrue(hasattr(user_test, "last_name"))
        self.assertTrue(hasattr(user_test, "save"))
        self.assertTrue(hasattr(user_test, "to_dict"))

    def test_user_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        user_test = User()
        self.assertEqual(user_test.email, "")
        self.assertEqual(user_test.first_name, "")
        self.assertEqual(user_test.last_name, "")
        self.assertEqual(user_test.password, "")

    def test_user_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        user_test = User()
        self.assertIsInstance(user_test.id, str)
        self.assertIsInstance(user_test.created_at, datetime)
        self.assertIsInstance(user_test.updated_at, datetime)
        self.assertIsInstance(user_test.password, str)
        self.assertIsInstance(user_test.email, str)
        self.assertIsInstance(user_test.first_name, str)
        self.assertIsInstance(user_test.last_name, str)

    def test_user_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        user_test = User()
        self.assertTrue(issubclass(type(user_test), BaseModel))

    def test_user_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        user_test = User()
        display = "[{:s}] ({:s}) {}\n".format(
                type(user_test).__name__, user_test.id,
                user_test.__dict__)
        print(user_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_user_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        user_test = User()
        self.assertEqual(user_test.created_at,
                         user_test.updated_at)
        user_test.save()
        self.assertNotEqual(user_test.created_at,
                            user_test.updated_at)

    def test_user_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        user_test = User()
        self.assertTrue(hasattr(user_test, "id"))
        self.assertTrue(hasattr(user_test, "created_at"))
        self.assertTrue(hasattr(user_test, "updated_at"))
        self.assertTrue(hasattr(user_test, "email"))
        self.assertTrue(hasattr(user_test, "password"))
        self.assertTrue(hasattr(user_test, "first_name"))
        self.assertTrue(hasattr(user_test, "last_name"))

    def test_user_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        user_test = User(*args)
        self.assertTrue(hasattr(user_test, "id"))
        self.assertTrue(hasattr(user_test, "created_at"))
        self.assertTrue(hasattr(user_test, "updated_at"))
        self.assertTrue(hasattr(user_test, "email"))
        self.assertTrue(hasattr(user_test, "password"))
        self.assertTrue(hasattr(user_test, "first_name"))
        self.assertTrue(hasattr(user_test, "last_name"))
        self.assertFalse(hasattr(user_test, "name"))
        self.assertFalse(hasattr(user_test, "age"))

    def test_user_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        user_test = User(*args, **dictionary)
        dictionary = user_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertTrue("email" in dictionary)
        self.assertTrue("password" in dictionary)
        self.assertTrue("first_name" in dictionary)
        self.assertTrue("last_name" in dictionary)

        dictionary["email"] = "alx_is_cool@gmail.com"
        dictionary["first_name"] = "Alexander"
        dictionary["last_name"] = "Iris"
        dictionary["password"] = "fakepassword1234"

        user_test = User(**dictionary)
        self.assertEqual(user_test.id, dictionary["id"])
        self.assertEqual(user_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(user_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(user_test.email, dictionary["email"])
        self.assertEqual(user_test.first_name, dictionary["first_name"])
        self.assertEqual(user_test.last_name, dictionary["last_name"])
        self.assertEqual(user_test.password, dictionary["password"])

        self.assertIsInstance(user_test, User)
        self.assertIsInstance(user_test.id, str)
        self.assertIsInstance(user_test.created_at, datetime)
        self.assertIsInstance(user_test.updated_at, datetime)
        self.assertIsInstance(user_test.email, str)
        self.assertIsInstance(user_test.first_name, str)
        self.assertIsInstance(user_test.last_name, str)
        self.assertIsInstance(user_test.password, str)
