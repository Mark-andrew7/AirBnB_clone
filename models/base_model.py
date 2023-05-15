#!/usr/bin/python3
from datetime import datetime
import uuid
import models


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
                if k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
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
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

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
        dict_cpy = self.__dict__.copy()
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        dict_cpy["__class__"] = self.__class__.__name__
        return dict_cpy
