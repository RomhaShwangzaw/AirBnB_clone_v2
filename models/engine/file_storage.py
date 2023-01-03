#!/usr/bin/python3
''' Storage module '''

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    ''' A `FileStorage` class that serializes instances to a
        JSON file and deserializes JSON file to instances.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary `__objects` '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        odict = FileStorage.__objects
        objdict = {k: v.to_dict() for k, v in odict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        ''' deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists; otherwise, do nothing. If the
            file doesn’t exist, no exception should be raised).
        '''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for k, o in objdict.items():
                    cls_name = o["__class__"]
                    obj = self.new(eval(cls_name)(**o))
