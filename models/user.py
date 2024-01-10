#!/usr/bin/python3
""" Define a user class"""

from models.base_model import BaseModel


class User (BaseModel):
    """ Defines class user inheriting from BaseModel."""

    def __init__(self):
        """ Initialize a new user"""

        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
