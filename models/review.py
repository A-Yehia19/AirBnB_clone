#!/usr/bin/python3
""" Define a review class"""

from models.base_model import BaseModel


class Review (BaseModel):
    """ Defines class review inheriting from BaseModel."""

    place_id = ""
    user_id = ""
    text = ""
