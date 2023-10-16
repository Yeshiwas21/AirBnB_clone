#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel

class User(BaseModel):
    """
    The User class inherits from BaseModel and represents a User object.

    Public instance attributes:
    - username: string - the user's username.
    - email: string - the user's email.

    Additional user-specific attributes can be added as needed.
    """
    
    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email
        # Additional user-specific attributes can be added here
