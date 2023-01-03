#!/usr/bin/python3
"""
This module creates a State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that inherits from BaseModel for managing state objects"""
    name = ""
