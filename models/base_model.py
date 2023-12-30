#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Define the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of BaseModel."""
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            storage.new(self)
            return
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
