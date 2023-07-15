#!/usr/bin/python3
import unittest
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests for file storage class
    and some Base Model updates"""

    def setUp(self):
        """Setup testing objects"""
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """Tear down test object"""
        self.storage = None
        self.my_model = None

    def test_new(self):
        """Test that 'new' method adds objects to __objects"""
        initial_storage_state = storage.all().copy()
        new_obj = BaseModel()
        storage.new(new_obj)
        new_storage_state = storage.all()

        new_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertNotEqual(initial_storage_state, new_storage_state)
        self.assertTrue(new_key in new_storage_state)

    def test_save(self):
        """Test that 'save' method serializes objects to JSON file"""
        self.my_model.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test that 'reload' method deserializes JSON files to __objects"""
        try:
            self.storage.reload()
        except Exception as e:
            self.fail("test_reload failed: {}".format(str(e)))


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

if __name__ == "__main__":
    unittest.main()
