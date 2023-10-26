#!/bin/usr/python3
"""File Storage"""
import json
from models.base_model import BaseModel
class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Stores the object in the __objects dictionary with a key based on the <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serialize __objects to the json file"""
        self.updated_at = datetime.datetime.now()

    def reload(self):
        """deserializes __objects to the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = json.load(file)
        except:
            pass