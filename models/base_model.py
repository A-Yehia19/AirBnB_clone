#!/usr/bin/python3
""" Define a base model class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Defines  all common attributes/methods for other classes."""

    def __init__(self):
        """ Initialize a new model."""

        self.id = str(uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


    def __str__(self):
        """ Return representation of BaseModel"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates  updated_at with the current datetime"""

        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
