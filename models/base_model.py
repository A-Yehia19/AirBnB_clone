#!/usr/bin/python3
""" Define a base model class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines  all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """ Initialize a new model."""

        if kwargs:
            for key, value in kwargs.items():
                # convert string to datetime
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                # add all elements and ignore class attribute
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Return representation of BaseModel"""

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""

        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()

        return class_dict
