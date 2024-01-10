#!/usr/bin/python3
""" Define a state class"""

from models.base_model import BaseModel


class State (BaseModel):
    """ Defines class state inheriting from BaseModel."""

    def __init__(self):
        """ Initialize a new state"""

        super().__init__()
        self.name = ""
