#!/usr/bin/python3
"""FileStorage Module"""


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = self.__objects
        my_obj = {}

        for key in objects.keys():
            my_obj[key] = objects[key].to_dict()

        with open(self.__file_path, 'w') as my_file:
            json.dump(my_obj, my_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as my_file:
                obj_dicts = json.load(my_file)
                for key, values in obj_dicts.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**values)
                    self.__objects[key] = instance
