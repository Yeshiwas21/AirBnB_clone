#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.

    Public instance methods:
    - test_str_representation(): Test the __str__ representation of BaseModel.
    - test_save_method(): Test the save method for BaseModel.
    - test_to_dict_method(): Test the to_dict method for BaseModel.
    """
    
    def setUp(self):
        self.base_model = BaseModel()

    def test_str_representation(self):
        """
        Test the __str__ representation of BaseModel.
        """
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """
        Test the save method for BaseModel.
        """
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method for BaseModel.
        """
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
