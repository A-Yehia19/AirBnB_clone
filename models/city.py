#!/usr/bin/python3
""" Define a city class"""

from models.base_model import BaseModel


class City (BaseModel):
    """ Defines class city inheriting from BaseModel."""

    state_id = ""
    name = ""
