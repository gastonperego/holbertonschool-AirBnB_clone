#!/bin/usr/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """file storage class"""
    add_class = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Stores the object in the __objects dictionary
        with a key based on the <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serialize __objects to the json file"""
        for key in self.__objects.keys():
            self.__objects[key] = str(self.__objects[key])

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """deserializes __objects to the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = json.load(file)
        except Exception:
            pass
