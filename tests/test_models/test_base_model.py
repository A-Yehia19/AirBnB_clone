#!/usr/bin/python3
""" test of BaseModel class """

import unittest
from models import base_model as base_model_module
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test BaseModel Class """

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(base_model_module.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
