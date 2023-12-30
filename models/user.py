#!/usr/bin/python3
"""
User Class
==========

This module defines the User class, which represents a user in a user management system.

The User class inherits from the BaseModel class and is used to store information about users.

Attributes:
    username (str): The user's username.
    email (str): The user's email address.
    (You can add additional user-specific attributes as needed.)

"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
