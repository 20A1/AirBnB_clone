#!/usr/bin/python3
"""
This module contains the several unit tests for the 'State' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
State = __import__('models.state').state.State
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestState(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'State'
    class
    """

    def test_state_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        state1 = State()
        state2 = State()
        self.assertTrue(hasattr(state1, "id"))
        self.assertTrue(hasattr(state2, "id"))
        self.assertNotEqual(state1.id, state2.id)
        self.assertIsInstance(state1.id, str)
        self.assertIsInstance(state2.id, str)

    def test_state_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        state_test = State()
        self.assertTrue(hasattr(state_test, "id"))
        self.assertTrue(hasattr(state_test, "created_at"))
        self.assertTrue(hasattr(state_test, "updated_at"))
        self.assertTrue(hasattr(state_test, "name"))
        self.assertTrue(hasattr(state_test, "save"))
        self.assertTrue(hasattr(state_test, "to_dict"))

    def test_state_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        state_test = State()
        self.assertEqual(state_test.name, "")

    def test_state_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        state_test = State()
        self.assertIsInstance(state_test.id, str)
        self.assertIsInstance(state_test.created_at, datetime)
        self.assertIsInstance(state_test.updated_at, datetime)
        self.assertIsInstance(state_test.name, str)

    def test_state_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        state_test = State()
        self.assertTrue(issubclass(type(state_test), BaseModel))

    def test_state_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        state_test = State()
        display = "[{:s}] ({:s}) {}\n".format(
                type(state_test).__name__, state_test.id,
                state_test.__dict__)
        print(state_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_state_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        state_test = State()
        self.assertEqual(state_test.created_at,
                         state_test.updated_at)
        state_test.save()
        self.assertNotEqual(state_test.created_at,
                            state_test.updated_at)

    def test_state_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        state_test = State()
        self.assertTrue(hasattr(state_test, "id"))
        self.assertTrue(hasattr(state_test, "created_at"))
        self.assertTrue(hasattr(state_test, "updated_at"))
        self.assertTrue(hasattr(state_test, "name"))
        self.assertFalse(hasattr(state_test, "email"))
        self.assertFalse(hasattr(state_test, "password"))
        self.assertFalse(hasattr(state_test, "first_name"))
        self.assertFalse(hasattr(state_test, "last_name"))

    def test_state_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        state_test = State(*args)
        self.assertTrue(hasattr(state_test, "id"))
        self.assertTrue(hasattr(state_test, "created_at"))
        self.assertTrue(hasattr(state_test, "updated_at"))
        self.assertTrue(hasattr(state_test, "name"))
        self.assertFalse(hasattr(state_test, "email"))
        self.assertFalse(hasattr(state_test, "password"))
        self.assertFalse(hasattr(state_test, "first_name"))
        self.assertFalse(hasattr(state_test, "last_name"))
        self.assertFalse(hasattr(state_test, "age"))

    def test_state_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        state_test = State(*args, **dictionary)
        dictionary = state_test.to_dict()

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

        state_test = State(**dictionary)
        self.assertEqual(state_test.id, dictionary["id"])
        self.assertEqual(state_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(state_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(state_test.name, dictionary["name"])

        self.assertIsInstance(state_test, State)
        self.assertIsInstance(state_test.id, str)
        self.assertIsInstance(state_test.created_at, datetime)
        self.assertIsInstance(state_test.updated_at, datetime)
        self.assertIsInstance(state_test.name, str)
