#!/usr/bin/python3
"""
State Class
===========

This module defines the State class, which represents a state in a property management system.

Attributes:
    name (str): The name of the state.

"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, name=""):
        """
        Constructor for the State class.

        :param name: The name of the state. (default is an empty string)
        :type name: str
        """
        super().__init__()
        self.name = name
