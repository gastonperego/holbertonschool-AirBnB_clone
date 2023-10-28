#!/usr/bin/python3
"""Basemodel"""
import datetime
import uuid
import models


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ("created_at", "update_at"):
                    value = datetime.datetime.fromisoformat(str(value))
                    setattr(self, key, value)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """this is the representation of string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update_at is responsible for updating to the current time."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """this is the dictionary with the keys/values of the instance"""
        dic = {}
        dic.update(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = str(self.created_at)
        dic['updated_at'] = str(self.updated_at)
        return dic
