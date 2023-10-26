#!/bin/usr/python3
"""File Storage"""
import json

class FileStrorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """Stores the object in the __objects dictionary with a key based on the <obj class name>.id"""
        self.__objects[f"{obj.__name__}.{obj.id}"] = obj


    def save(self):
        """serialize __objects to the json file"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(data, json_file)
    
    def reload(self):
        """deserializes __objects to the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = json.load(file)
        except:
            pass
            