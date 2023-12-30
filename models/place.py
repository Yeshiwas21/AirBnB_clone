#!/usr/bin/python3
"""
Place Class
===========

This module defines the Place class, which represents a place in a property management system.

Attributes:
    city_id (str): The City ID associated with the place.
    user_id (str): The User ID associated with the place.
    name (str): The name of the place.
    description (str): A description of the place.
    number_rooms (int): The number of rooms in the place.
    number_bathrooms (int): The number of bathrooms in the place.
    max_guest (int): The maximum number of guests allowed in the place.
    price_by_night (int): The price per night for the place.
    latitude (float): The latitude of the place.
    longitude (float): The longitude of the place.
    amenity_ids (list): A list of Amenity IDs associated with the place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for managing place objects"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
