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
    """
    Represents a place.

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

    def __init__(self, city_id="", user_id="", name="", description="",
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0, amenity_ids=[]):
        """
        Constructor for the Place class.

        :param city_id: The City ID associated with the place. (default is an empty string)
        :type city_id: str
        :param user_id: The User ID associated with the place. (default is an empty string)
        :type user_id: str
        :param name: The name of the place. (default is an empty string)
        :type name: str
        :param description: A description of the place. (default is an empty string)
        :type description: str
        :param number_rooms: The number of rooms in the place. (default is 0)
        :type number_rooms: int
        :param number_bathrooms: The number of bathrooms in the place. (default is 0)
        :type number_bathrooms: int
        :param max_guest: The maximum number of guests allowed in the place. (default is 0)
        :type max_guest: int
        :param price_by_night: The price per night for the place. (default is 0)
        :type price_by_night: int
        :param latitude: The latitude of the place. (default is 0.0)
        :type latitude: float
        :param longitude: The longitude of the place. (default is 0.0)
        :type longitude: float
        :param amenity_ids: A list of Amenity IDs associated with the place. (default is an empty list)
        :type amenity_ids: list
        """
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
