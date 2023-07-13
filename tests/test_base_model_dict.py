#!/usr/bin/python3
import datetime
import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test case of the Base model dict task"""

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


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".
          format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
