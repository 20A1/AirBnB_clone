#!/usr/bin/python3
"""
This module contains the several unit tests for the 'BaseModel' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'BaseModel'
    class
    """

    def test_base_model_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertTrue(hasattr(base_model1, "id"))
        self.assertTrue(hasattr(base_model2, "id"))
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertIsInstance(base_model1.id, str)
        self.assertIsInstance(base_model2.id, str)

    def test_base_model_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        base_model_test = BaseModel()
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))
        self.assertTrue(hasattr(base_model_test, "save"))
        self.assertTrue(hasattr(base_model_test, "to_dict"))

    def test_base_model_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        base_model_test = BaseModel()
        self.assertIsInstance(base_model_test.created_at, datetime)
        self.assertIsInstance(base_model_test.updated_at, datetime)

    def test_base_model_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        base_model_test = BaseModel()
        display = "[{:s}] ({:s}) {}\n".format(
                type(base_model_test).__name__, base_model_test.id,
                base_model_test.__dict__)
        print(base_model_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_base_model_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        base_model_test = BaseModel()
        self.assertEqual(base_model_test.created_at,
                         base_model_test.updated_at)
        base_model_test.save()
        self.assertNotEqual(base_model_test.created_at,
                            base_model_test.updated_at)

    def test_base_model_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        base_model_test = BaseModel()
        self.assertTrue(hasattr(base_model_test, "id"))
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))

    def test_base_model_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        base_model_test = BaseModel(*args)
        self.assertTrue(hasattr(base_model_test, "id"))
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))
        self.assertFalse(hasattr(base_model_test, "name"))
        self.assertFalse(hasattr(base_model_test, "age"))

    def test_base_model_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        base_model_test = BaseModel(*args, **dictionary)
        dictionary = base_model_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)

        base_model_test = BaseModel(**dictionary)
        self.assertEqual(base_model_test.id, dictionary["id"])
        self.assertEqual(base_model_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(base_model_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertIsInstance(base_model_test, BaseModel)
        self.assertIsInstance(base_model_test.created_at, datetime)
        self.assertIsInstance(base_model_test.updated_at, datetime)
