#!/usr/bin/python3
"""
FileStorage Class
=================

This module defines the FileStorage class, which is responsible for saving and loading objects to/from a JSON file.

Attributes:
    __file_path (str): The name of the file to save objects to.
    __objects (dict): A dictionary of instantiated objects.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Represents an abstracted storage engine for saving and loading objects.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the internal dictionary __objects with a key of <obj_class_name>.id."""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize the objects in __objects and save them to the JSON file defined by __file_path."""
        obj_dict = FileStorage.__objects
        serialized_objects = {key: obj.to_dict() for key, obj in obj_dict.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file defined by __file_path and populate __objects with the loaded objects."""
        try:
            with open(FileStorage.__file_path) as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError:
            return
