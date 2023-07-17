#!/usr/bin/python3
""" file storage class"""
import json
import os.path as path
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
        if obj:
            k = obj.__class__.__name__ + str(obj.id)
            self.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the json file
        """
        obj_dict = {}
        with open(self.__file_path, "w", encoding="UTF-8") as file:
            for k, v in self.__objects.items():
                obj_dict[k] = v.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """convert existing json  dicts to instances"""
        try:
            if path.isfile(self.__file_path):
                with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                    for key, value in json.load(f).items():
                        value = eval(value['__class__'])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
