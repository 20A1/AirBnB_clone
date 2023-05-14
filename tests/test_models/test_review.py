#!/usr/bin/python3
"""
This module contains the several unit tests for the 'Review' class.

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
Review = __import__('models.review').review.Review
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestReview(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'Place'
    class
    """

    def test_review_id(self):
        """
        Test to ensure the uniqueness of the object's id attribute, as well as
        the presence of the attribute and it's data type
        """

        review1 = Review()
        review2 = Review()
        self.assertTrue(hasattr(review1, "id"))
        self.assertTrue(hasattr(review2, "id"))
        self.assertNotEqual(review1.id, review2.id)
        self.assertIsInstance(review1.id, str)
        self.assertIsInstance(review2.id, str)

    def test_review_attributes(self):
        """
        Test to verify that the required attributes exists in the class
        """

        review_test = Review()
        self.assertTrue(hasattr(review_test, "id"))
        self.assertTrue(hasattr(review_test, "created_at"))
        self.assertTrue(hasattr(review_test, "updated_at"))
        self.assertTrue(hasattr(review_test, "place_id"))
        self.assertTrue(hasattr(review_test, "user_id"))
        self.assertTrue(hasattr(review_test, "text"))
        self.assertTrue(hasattr(review_test, "save"))
        self.assertTrue(hasattr(review_test, "to_dict"))

    def test_review_attributes_value(self):
        """
        Test to verify that the required attributes are set to the default
        values for the object
        """

        review_test = Review()
        self.assertEqual(review_test.place_id, "")
        self.assertEqual(review_test.user_id, "")
        self.assertEqual(review_test.text, "")

    def test_review_attributes_type(self):
        """
        Test to verify the data types of the class attributes
        """

        review_test = Review()
        self.assertIsInstance(review_test.id, str)
        self.assertIsInstance(review_test.created_at, datetime)
        self.assertIsInstance(review_test.updated_at, datetime)
        self.assertIsInstance(review_test.place_id, str)
        self.assertIsInstance(review_test.user_id, str)
        self.assertIsInstance(review_test.text, str)

    def test_review_subclass(self):
        """
        Test to verify that place is a subclass of the 'BaseModel' class
        """

        review_test = Review()
        self.assertTrue(issubclass(type(review_test), BaseModel))

    def test_review_str(self):
        """
        Test to verify that the '__str__' function of the class has been
        properly overridden and displays the right information in the right
        format when pass to the 'print' function
        """

        self.maxDiff = None
        captured_output = io.StringIO()
        sys.stdout = captured_output
        review_test = Review()
        display = "[{:s}] ({:s}) {}\n".format(
                type(review_test).__name__, review_test.id,
                review_test.__dict__)
        print(review_test)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display)

    def test_review_datetimes(self):
        """
        Test to verify the two datatime attributes 'created_at' and
        'updated_at' are the same upon when created and different when the
        object is updated
        """

        review_test = Review()
        self.assertEqual(review_test.created_at,
                         review_test.updated_at)
        review_test.save()
        self.assertNotEqual(review_test.created_at,
                            review_test.updated_at)

    def test_review_constructors1(self):
        """
        Test to verify that the first constructor of the class i.e no parameter
        passed, works as expected and initialized attributes to their default
        value
        """

        review_test = Review()
        self.assertTrue(hasattr(review_test, "id"))
        self.assertTrue(hasattr(review_test, "created_at"))
        self.assertTrue(hasattr(review_test, "updated_at"))
        self.assertTrue(hasattr(review_test, "place_id"))
        self.assertTrue(hasattr(review_test, "user_id"))
        self.assertTrue(hasattr(review_test, "text"))

    def test_review_constructors2(self):
        """
        Test to verify that the second constructor of the class i.e *args
        parameter passed, works as expected and initialized attributes to
        their default value ignoring the args parameter
        """

        args = ("LQ McDonald", 22)
        review_test = Review(*args)
        self.assertTrue(hasattr(review_test, "id"))
        self.assertTrue(hasattr(review_test, "created_at"))
        self.assertTrue(hasattr(review_test, "updated_at"))
        self.assertTrue(hasattr(review_test, "place_id"))
        self.assertTrue(hasattr(review_test, "user_id"))

    def test_review_constructors3(self):
        """
        Test to verify that the third constructor of the class i.e **kwargs
        parameter passed, works as expected and initialized attributes to the
        corresponding value of the dictionary passed, where the keys name are
        the names of the class attributes
        """

        dictionary = {}
        args = ("Aisha Owolabi", 28)
        review_test = Review(*args, **dictionary)
        dictionary = review_test.to_dict()

        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertTrue("place_id" in dictionary)
        self.assertTrue("user_id" in dictionary)
        self.assertTrue("text" in dictionary)

        dictionary["place_id"] = "1212-1212-1212-1212"
        dictionary["user_id"] = "1234-1234-1234-1234"
        dictionary["text"] = "A nice environment with a great outdoor feel"

        review_test = Review(**dictionary)
        self.assertEqual(review_test.id, dictionary["id"])
        self.assertEqual(review_test.created_at,
                         datetime.fromisoformat(dictionary["created_at"]))
        self.assertEqual(review_test.updated_at,
                         datetime.fromisoformat(dictionary["updated_at"]))
        self.assertEqual(review_test.place_id, dictionary["place_id"])
        self.assertEqual(review_test.user_id, dictionary["user_id"])
        self.assertEqual(review_test.text, dictionary["text"])

        self.assertIsInstance(review_test, Review)
        self.assertIsInstance(review_test.created_at, datetime)
        self.assertIsInstance(review_test.updated_at, datetime)
        self.assertIsInstance(review_test.place_id, str)
        self.assertIsInstance(review_test.user_id, str)
        self.assertIsInstance(review_test.text, str)
