#!/usr/bin/python3
""" test of State class """

import unittest
from models import state as state_module
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test State Class """

    def setUp(self):
        """ Create instance global  """
        self.state = State()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(state_module.__doc__)
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_inheritance(self):
        """ Test if State subclasses of BaseModel """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.state, "name"))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.state.name), str)


if __name__ == '__main__':
    unittest.main()
