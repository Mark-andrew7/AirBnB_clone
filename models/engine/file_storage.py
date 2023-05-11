#!/usr/bin/python3


class FileStorage:
    """
    class that serializes instances to json file
    """
    __file_path = file.json
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
