#!/usr/bin/python3
"""
Amenity Class
=============

This module defines the Amenity class, which represents an amenity in a property management system. An amenity can have a name.

Attributes:
    name (str): The name of the amenity.

"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    def __init__(self, name=""):
        """
        Constructor for the Amenity class.

        :param name: The name of the amenity. (default is an empty string)
        :type name: str
        """
        super().__init__()
        self.name = name
