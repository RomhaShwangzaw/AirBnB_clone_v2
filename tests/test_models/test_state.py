#!/usr/bin/python3
"""
Unittest module for the Review Class
"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ Test Cases for the State class """

    def testClassDocumentation(self):
        """
            Test to check Class documentation
        """
        self.assertGreater(len(State.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Test to check Constructor documentation
        """
        self.assertGreater(len(State.__init__.__doc__), 0)

    def testConstructor(self):
        """
            Constructor test
        """
        s1 = State()
        s1.name = "Daniel"
        s1.save()
        self.assertGreater(s1.updated_at, s1.created_at)
        self.assertDictEqual(
            s1.to_dict(),
            {
                'id': s1.id,
                'created_at': s1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': s1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Daniel",
                '__class__': 'State'
            }
        )

    def testNameType(self):
        """
            Check name attribute type
        """
        self.assertIsInstance(State().name, str)


if __name__ == "__main__":
    unittest.main()
