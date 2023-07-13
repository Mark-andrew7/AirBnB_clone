#!/usr/bin/python3
import unittest
import datetime
import time
from models import base_model
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test cases for Base Model"""

    def setUp(self):
        """set up"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down"""
        pass

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
        before_save = self.model.updated_at
        time.sleep(0.001)
        self.model.save()
        self.assertNotEqual(before_save, self.model.updated_at)

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


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}"
          .format(key, type(my_model_json[key]), my_model_json[key]))
