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
    """
    Represents a city.

    Attributes:
        state_id (str): The state ID of the city.
        name (str): The name of the city.
    """

    def __init__(self, state_id="", name=""):
        """
        Constructor for the City class.

        :param state_id: The state ID of the city. (default is an empty string)
        :type state_id: str
        :param name: The name of the city. (default is an empty string)
        :type name: str
        """
        super().__init__()
        self.state_id = state_id
        self.name = name
