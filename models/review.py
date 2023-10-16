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
    """
    Represents a review.

    Attributes:
        place_id (str): The Place ID associated with the review.
        user_id (str): The User ID associated with the review.
        text (str): The text of the review.
    """

    def __init__(self, place_id="", user_id="", text=""):
        """
        Constructor for the Review class.

        :param place_id: The Place ID associated with the review. (default is an empty string)
        :type place_id: str
        :param user_id: The User ID associated with the review. (default is an empty string)
        :type user_id: str
        :param text: The text of the review. (default is an empty string)
        :type text: str
        """
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
