#!/usr/bin/python3
"""review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""
    place_id = ''
    user_id = ''
    text = ''
