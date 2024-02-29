#!/usr/bin/python3


import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

        FileStorage._FileStorage__objects = {}
    
    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def test_all(self):      
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()

        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        self.storage.save()
        file_path = "file.json"

        with open(file_path, 'r') as f:
            lines = f.readlines()

        os.remove(file_path)
        self.storage.save()

        with open(file_path, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        with open(file_path, "w") as f:
            f.write("{}")

        with open(file_path, "r") as r:
            self.assertEqual(r.read(), "{}")

        self.assertIs(self.storage.reload(), None)
        os.remove(file_path)
