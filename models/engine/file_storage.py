#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    class that serializes instances to json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns dict objects __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in object with a key
        """
        k = obj.__class__.__name__ + "."
        key = k + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the json file
        """
        obj_dict = {}
        for k, v in self.__objects.items:
            obj_dict[k] = v.to_dict()

        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes json file to __objects file
        """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                cls_name = k.split('.')
                Class = eval(cls_name)
                instance = Class(**v)
                self.__objects[k] = instance
        except FileNotFoundError:
            pass
