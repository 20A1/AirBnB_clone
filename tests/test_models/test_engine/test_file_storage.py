#!/usr/bin/python3
"""
This Module contains several unit tests for the 'FileStorage' class

These tests help ensure the implementation of the class works as expected and
helps in ensuring that buggy code are rectified.
"""


import unittest
import sys
sys.path.append('../../../models/engine')
FileStorage = __import__('models.engine.file_storage').file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """
    A unit test class that inherits from the 'unittest.TestCase' class as is
    required of all unit tests and contains several tests for the 'FileStorage'
    class
    """

    def test_file_storage_attributes(self):
        """
        Tests that the FileStorage object has the expected attributes
        """
        file_storage_tests = FileStorage()
        self.assertTrue(hasattr(file_storage_tests, "_FileStorage__file_path"))
        self.assertTrue(hasattr(file_storage_tests, "_FileStorage__objects"))

    def test_file_storage_methods(self):
        """
        Tests that the FileStorage object has the expected methods
        """
        file_storage_tests = FileStorage()
        self.assertTrue(hasattr(file_storage_tests, "all"))
        self.assertTrue(hasattr(file_storage_tests, "new"))
        self.assertTrue(hasattr(file_storage_tests, "save"))
        self.assertTrue(hasattr(file_storage_tests, "reload"))

    def test_file_storage_attribute_types(self):
        """
        Test that the data types of the attributes in the FileSotorage class
        are the right type
        """
        file_storage_tests = FileStorage()
        self.assertIsInstance(file_storage_tests._FileStorage__file_path, str)
        self.assertIsInstance(file_storage_tests._FileStorage__objects, dict)

    def test_file_storage_method_types(self):
        """
        Test that the data types of the attributes in the FileSotorage class
        are the right type
        """
        file_storage_tests = FileStorage()
        self.assertTrue(callable(file_storage_tests.new))
        self.assertTrue(callable(file_storage_tests.all))
        self.assertTrue(callable(file_storage_tests.save))
        self.assertTrue(callable(file_storage_tests.reload))
