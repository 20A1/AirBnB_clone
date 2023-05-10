#!/usr/bin/python3
"""
Import the 'file_storage' module from the 'engine' subpackage and also
initialize the storage variable for the 'models' package modules to use for
saving operations
"""


from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
