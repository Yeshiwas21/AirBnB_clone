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
    """Class for managing state objects"""

    name = ""
