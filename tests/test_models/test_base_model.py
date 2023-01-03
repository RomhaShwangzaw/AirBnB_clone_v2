#!/usr/bin/python3
""" Unittest module for the base_model class """
from models.base_model import BaseModel
import unittest
from datetime import datetime
import time


class BaseModelTest(unittest.TestCase):
    """ Test Cases for the BaseModel class """

    def testClassDocumentation(self):
        """
            Test to check for class documentation
        """
        self.assertGreater(len(BaseModel.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Test to check for constructor documentation
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def testStrDocumentation(self):
        """
            Test to check if __str__ function have documentation
        """
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

    def testSaveDocumentation(self):
        """
            Test to check if save function have documentation
        """
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def testToDictDocumentation(self):
        """
            Test to check if to_dict function have documentation
        """
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def testStr(self):
        """
            Test __str__ function
        """
        b1 = BaseModel()
        b1.name = "Daniel"
        b1.my_number = 11
        b1.my_wrong_test = None
        self.assertEqual(
            b1.__str__(), "[{}] ({}) {}".format(
                b1.__class__.__name__,
                b1.id,
                b1.__dict__
            )
        )

    def testSave(self):
        """
            Test save function
        """
        import os
        import json
        from models import storage

        b1 = BaseModel()
        b1.name = "Daniel"
        b1.my_number = 11
        b1.my_wrong_test = None
        b1.save()
        self.assertGreater(b1.updated_at, b1.created_at)
        self.assertDictEqual(
            b1.to_dict(),
            {
                '__class__': 'BaseModel',
                'created_at': b1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'id': b1.id,
                'my_number': 11,
                'my_wrong_test': None,
                'name': "Daniel",
                'updated_at': b1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            }
        )

        tmpDict = {}
        for key, value in storage.all().items():
            tmpDict[key] = value.to_dict()
        b1 = BaseModel()
        key = "{}.{}".format("BaseModel", b1.id)
        storage.new(b1)
        b1.save()
        tmpDict[key] = b1.to_dict()
        inputStr = json.dumps(tmpDict)
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            output = file.read()
        self.assertEqual(json.loads(inputStr), json.loads(output))


if __name__ == "__main__":
    unittest.main()
