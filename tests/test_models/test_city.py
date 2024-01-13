#!/usr/bin/python3
""" test of City class """

import unittest
from models import city as city_module
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Test City Class """

    def setUp(self):
        """ Create instance global  """
        self.city = City()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(city_module.__doc__)
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_inheritance(self):
        """ Test if City subclasses of BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)


if __name__ == '__main__':
    unittest.main()
