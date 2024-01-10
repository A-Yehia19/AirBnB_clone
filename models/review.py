#!/usr/bin/python3
""" Define a review class"""

from models.base_model import BaseModel


class Review (BaseModel):
    """ Defines class review inheriting from BaseModel."""

    def __init__(self):
        """ Initialize a new review"""

        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
