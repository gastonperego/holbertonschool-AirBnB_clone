#!/usr/bin/python3
"""Basemodel"""
import datetime
import uuid

class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ("created_at", "update_at"):
                    value = datetime.datetime.fromisoformat(str(value))
                    setattr(self, key, value)
 
    def __str__(self):
        """this is the representation of string"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at is responsible for updating to the current time."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """this is the dictionary with the keys/values of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = str(self.created_at.isoformat())
        dic['updated_at'] = str(self.updated_at.isoformat())
        return dic