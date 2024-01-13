#!/usr/bin/python3
""" test of Place class """

import unittest
from models import place as place_module
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test Place Class """

    def setUp(self):
        """ Create instance global  """
        self.place = Place()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(place_module.__doc__)
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_inheritance(self):
        """ Test if Place subclasses of BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
