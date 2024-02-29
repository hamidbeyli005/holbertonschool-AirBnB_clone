#!/usr/bin/python3
"""User tests"""


import unittest
import os

from models.user import User
from models import storage


class TestUserModel(unittest.TestCase):
    def setUp(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.__objects = {}

    def test_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        user = User()
        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

    def test_password(self):
        user = User()
        user.password = "password123"
        self.assertEqual(user.password, "password123")

    def test_first_name(self):
        user = User()
        user.first_name = "Hamid"
        self.assertEqual(user.first_name, "Hamid")

    def test_last_name(self):
        user = User()
        user.last_name = "Hamidbayli"
        self.assertEqual(user.last_name, "Hamidbayli")
