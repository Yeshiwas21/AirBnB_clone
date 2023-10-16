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
    """
    Represents a user.

    Attributes:
        username (str): The user's username.
        email (str): The user's email address.
        (You can add additional user-specific attributes as needed.)

    """

    def __init__(self, username, email):
        """
        Constructor for the User class.

        :param username: The user's username.
        :type username: str
        :param email: The user's email address.
        :type email: str

        (You can add additional user-specific attributes as needed.)
        """
        super().__init__()
        self.username = username
        self.email = email
        # Additional user-specific attributes can be added here
