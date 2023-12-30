#!/usr/bin/python3
"""Test cases for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Test creating BaseModel instance from dictionary representation."""

    def test_create_instance_from_dict(self):
        """Test creating BaseModel instance from dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(str(my_model), str(my_new_model))

if __name__ == '__main__':
    unittest.main()
