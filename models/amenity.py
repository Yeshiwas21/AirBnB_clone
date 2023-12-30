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
    """Class for managing amenity objects"""

    name = ""
