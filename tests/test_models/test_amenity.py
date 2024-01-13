#!/usr/bin/python3
""" test of Amenity class """

import unittest
from models import amenity as amenity_module
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test Amenity Class """

    def setUp(self):
        """ Create instance global  """
        self.amenity = Amenity()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(amenity_module.__doc__)
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_inheritance(self):
        """ Test if Amenity subclasses of BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.amenity.name), str)


if __name__ == '__main__':
    unittest.main()
