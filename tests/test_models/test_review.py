#!/usr/bin/python3
""" test of Review class """

import unittest
from models import review as review_module
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test Review Class """

    def setUp(self):
        """ Create instance global  """
        self.review = Review()

    def test_docstring(self):
        """ Test if all docstring were written """
        self.assertIsNotNone(review_module.__doc__)
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_inheritance(self):
        """ Test if Review subclasses of BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """ Check required attribute are created """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_types(self):
        """ test types of attributes """
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)


if __name__ == '__main__':
    unittest.main()
