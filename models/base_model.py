#!/usr/bin/python3
"""This module contains the base model
    from which all others class will inherit
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    This is the BaseModel class that defines common attributes/methods for other classes.

    Public instance attributes:
    - id: string - assign with a unique ID when an instance is created.
    - created_at: datetime - assign with the current datetime when an instance is created.
    - updated_at: datetime - assign with the current datetime when an instance is created and update it
      every time you change your object.

    Public instance methods:
    - save(self): updates the 'updated_at' attribute with the current datetime.
    - to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance.

    This class will be the first piece of the serialization/deserialization process to create a dictionary
    representation of our BaseModel objects.
    """
    
    def __init__(self):
        """
        Initialize a BaseModel instance with a unique ID, creation time, and update time.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
