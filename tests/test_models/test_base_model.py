#!/usr/bin/python3

import unittest
import sys
import io
from datetime import datetime
sys.path.append('../../models')
BaseModel = __import__('models.base_model').base_model.BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_id(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertTrue(hasattr(base_model1, "id"))
        self.assertTrue(hasattr(base_model2, "id"))
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertIsInstance(base_model1.id, str)

    def test_base_model_attributes(self):
        base_model_test = BaseModel()
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))

    def test_base_model_attributes_type(self):
        base_model_test = BaseModel()
        self.assertIsInstance(base_model_test.created_at, datetime)
        self.assertIsInstance(base_model_test.updated_at, datetime)

    def test_base_model_str(self):
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
        base_model_test = BaseModel()
        self.assertEqual(base_model_test.created_at,
                         base_model_test.updated_at)
        base_model_test.save()
        self.assertNotEqual(base_model_test.created_at,
                            base_model_test.updated_at)

    def test_base_model_constructors1(self):
        base_model_test = BaseModel()
        self.assertTrue(hasattr(base_model_test, "id"))
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))

    def test_base_model_constructors2(self):
        args = ("LQ McDonald", 22)
        base_model_test = BaseModel(*args)
        self.assertTrue(hasattr(base_model_test, "id"))
        self.assertTrue(hasattr(base_model_test, "created_at"))
        self.assertTrue(hasattr(base_model_test, "updated_at"))
        self.assertFalse(hasattr(base_model_test, "name"))
        self.assertFalse(hasattr(base_model_test, "age"))

    def test_base_model_constructors3(self):
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
