#!/usr/bin/python3
"""Base class tests"""

import unittest
from models.base_model import BaseModel


class TestStringMethods(unittest.TestCase):
    def test_init(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.updated_at)
        self.assertIsNotNone(instance.created_at)

    def test_save(self):
        instance = BaseModel()
        instance.save()
        obj = "BaseModel." + instance.id
        with open("file.json", "r") as my_file:
            self.assertIn(obj, my_file.read())

    def test_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
    
    def test_str(self):
        model = BaseModel()
        self.assertIn(model.id, str(model))

if __name__ == '__main__':
    unittest.main()
