#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.

    Public instance methods:
    - test_user_creation(): Test the creation of a User instance.
    """
    
    def test_user_creation(self):
        """
        Test the creation of a User instance.
        """
        user = User("john_doe", "john@example.com")
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")

if __name__ == '__main__':
    unittest.main()
