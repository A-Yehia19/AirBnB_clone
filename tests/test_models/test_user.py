#!/usr/bin/python3
""" test of User class """

import unittest
from models import user as user_module
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test User Class """

    def setUp(self):
        """ Create instance global  """
        self.user = User()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(user_module.__doc__)
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_inheritance(self):
        """ Test if State subclasses of BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)


if __name__ == '__main__':
    unittest.main()
