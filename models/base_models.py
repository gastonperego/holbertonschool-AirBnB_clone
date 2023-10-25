#!/usr/bin/python3
"""Basemodel"""
from datetime import datetime
import uuid

class BaseModel:
    """BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.today().isoformat())
        self.updated_at = str(datetime.datetime.today().isoformat())
 
    def __str__(self):
        """this is the representation of string"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at is responsible for updating to the current time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """this is the dictionary with the keys/values of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic