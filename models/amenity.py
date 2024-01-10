#!/usr/bin/python3
""" Define a amenity class"""

from models.base_model import BaseModel


class Amenity (BaseModel):
    """ Defines class amenity inheriting from BaseModel."""

    def __init__(self):
        """ Initialize a new amenity"""

        super().__init__()
        self.name = ""
