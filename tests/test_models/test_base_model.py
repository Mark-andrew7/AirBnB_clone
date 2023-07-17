#!/usr/bin/python3
""" Unit Test for BaseModel """
import datetime
import os
import unittest
import time
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test cases for Base Model"""

    def setUp(self):
        """set up"""
        self.model = BaseModel()
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        """Tear down"""
        self.model = None
        self.storage = None
        self.my_model = None

    def test_initiation(self):
        """Testing if the model is correctly created"""
        self.assertTrue(isinstance(self.model, BaseModel))

    def test_id_type_and_uniqueness(self):
        """Test if type of the id is string"""
        self.assertEqual(type(self.model.id), str)

        model2 = BaseModel()
        """test if the id is unique"""
        self.assertNotEqual(self.model.id, model2.id)

    def test_date(self):
        """Test if the created_at is present and of datetime instance"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

        """Test if the updated_at is present and of datetime instance"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

        """Test for uniqeness of updated at on save"""
        prev_date = self.model.updated_at
        time.sleep(0.001)
        self.model.save()
        self.assertNotEqual(prev_date, self.model.updated_at)

    def test_save(self):
        """Test is the save method updates the update attribute"""
        time_cr = self.model.created_at
        time.sleep(0.001)
        time_up = self.model.updated_at
        self.model.save()
        self.assertFalse(time_up == self.model.updated_at)
        self.assertTrue(time_cr == self.model.created_at)

    def test_str(self):
        """Test if __str__ is working and of correct format"""
        self.assertEqual(str(self.model), "[BaseModel] ({}) {}"
                         .format(self.model.id, self.model.__dict__))

    def test_to_dict(self):
        """Test if to_dict() returns dictionary"""
        self.assertEqual(type(self.model.to_dict()), dict)

        model_dict = self.model.to_dict()
        """Test if the 'created_at' is present and correctly formatted"""
        self.assertTrue(model_dict.get('created_at'))
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())

        """Test if the 'updated_at' is present and correctly formatted"""
        self.assertTrue(model_dict.get('updated_at'))
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

        """Test if the '__class__' is present and correct"""
        self.assertTrue(model_dict.get('__class__'))
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_kwargs_attribute_assignment(self):
        """Testing attribute assignment with kwargs.
        I do this by creating a dictionary with some values and pass
        it to the 'BaseMode' initializer function. Then i check if these
        values are correctly assigned as attributes to 'BaseModel' instance
        """
        kwargs = {"id": "123", "created_at": "2023-07-13T12:59:36.620743",
                  "updated_at": "2023-07-13T12:59:36.620743"}
        model = BaseModel(**kwargs)

        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at,
                         datetime.datetime(2023, 7, 13, 12, 59, 36, 620743))
        self.assertEqual(model.updated_at,
                         datetime.datetime(2023, 7, 13, 12, 59, 36, 620743))

    def test_class_not_attribute(self):
        """Testing that '__class__' is not assigned as attribute"""
        kwargs = {"__class__": "SomeClass"}
        model = BaseModel(**kwargs)

        self.assertNotIn("__class__", model.__dict__)

    def test_automatic_id_created_at(self):
        """Testing automatic 'id' and 'created_at' on new instance
        if no 'kwargs' are provided the 'BaseModel' should automatically assing
        an 'id' and 'created_at' attributes
        """
        model = BaseModel()

        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(isinstance(model.id, str))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(isinstance(model.created_at, datetime.datetime))

    def test_new(self):
        """Test that 'new' method adds objects to __objects"""
        initial_storage_state = storage.all().copy()
        new_obj = BaseModel()
        storage.new(new_obj)
        new_storage_state = storage.all()

        new_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertNotEqual(initial_storage_state, new_storage_state)
        self.assertTrue(new_key in new_storage_state)

    def test_reload(self):
        """Test that 'reload' method deserializes JSON files to __objects"""
        try:
            self.storage.reload()
        except Exception as e:
            self.fail("test_reload failed: {}".format(str(e)))
