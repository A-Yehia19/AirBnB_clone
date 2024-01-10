#!/usr/bin/python3
""" Define a city class"""

from models.base_model import BaseModel


class City (BaseModel):
    """ Defines class city inheriting from BaseModel."""

    def __init__(self):
        """ Initialize a new city"""

        super().__init__()
        self.state_id = ""
        self.name = ""
