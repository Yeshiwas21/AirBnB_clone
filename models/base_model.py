#!/usr/bin/python3
"""
This module contains the BaseModel class from which all other classes will inherit.
"""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializer for the BaseModel class."""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of this class."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def __repr__(self):
        """Return a string representation of this object."""
        return self.__str__()

    def save(self):
        """Save the object and update the updated_at attribute."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of this object."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
            **self.__dict__
        }
