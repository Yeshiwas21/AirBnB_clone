#!/usr/bin/python3
"""
City Class
==========

This module defines the City class, which represents a city in a property management system.

Attributes:
    state_id (str): The state ID of the city.
    name (str): The name of the city.

"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
