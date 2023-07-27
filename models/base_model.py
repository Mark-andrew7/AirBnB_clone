#!/usr/bin/python3
"""Base model class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    defining a class
    """
    def __init__(self, *args, **kwargs):
        """
        initializer
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        print class name and attributes
        """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates updated_at with the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionaries representing all keys/values
        """
        dict_cpy = dict(self.__dict__)
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        dict_cpy["__class__"] = self.__class__.__name__
        return dict_cpy
