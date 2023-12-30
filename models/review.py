#!/usr/bin/python3
"""
Review Class
============

This module defines the Review class, which represents a review in a property management system.

Attributes:
    place_id (str): The Place ID associated with the review.
    user_id (str): The User ID associated with the review.
    text (str): The text of the review.

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
