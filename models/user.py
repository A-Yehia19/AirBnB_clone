#!/usr/bin/python3
""" Define a user class"""

from models.base_model import BaseModel


class User (BaseModel):
    """ Defines class user inheriting from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
