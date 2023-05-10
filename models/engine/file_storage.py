#!/usr/bin/python3
"""
This module contains the 'FileStorage' class which handles data storing
operations such as saving, reloading, e.t.c
"""

import json
import os
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances

    Some of the attributes and methods used to accomplish this are:
        - __file_path: string - path to the JSON file (ex: 'file.json')
        - __objects: dictionary - empty but will store all objects by
        <class name>.id (ex: to store a BaseModel object with id=12121212, the
        key will be BaseModel.12121212)

        The above attributes are private and they belong to the class, Some
        public instance methods include:
        - all(self): returns the dictionary __objects
        - new(self, obj): sets in '__objects' the 'obj' with key
        <obj class name>.id
        - save(self): serializes '__objects' to the JSON file
        (path: __file_path)
        - reload(self): deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists; otherwise, do nothing
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary '__objects'
        """

        return (self.__objects)

    def new(self, obj):
        """
        sets in '__objects' the 'obj' with key '<obj class name>.id'
        """

        key = "{:s}.{:s}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes '__objects' to the JSON file (path: '__file_path')
        """

        json_ser = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as f:
            f.write(json_ser)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                read = f.read()
                self.__objects = json.loads(read)
