#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """Define the FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    value['created_at'] = datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    value['updated_at'] = datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_instance = BaseModel(**value) if class_name == 'BaseModel' else None
                    if obj_instance:
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
