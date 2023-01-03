#!/usr/bin/python3
"""
This module creates a Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that inherits from BaseModel for managing amenity objects"""
    name = ""
