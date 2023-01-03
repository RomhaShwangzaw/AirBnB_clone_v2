#!/usr/bin/python3
"""
Unittest module for the City Class
"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Test Cases for the City class """

    def testClassDocumentation(self):
        """
            Test for Class documentation
        """
        self.assertGreater(len(City.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Test for checking Constructor documentation
        """
        self.assertGreater(len(City.__init__.__doc__), 0)

    def testConstructor(self):
        """
            Constructor test
        """
        c1 = City()
        c1.name = "Daniel"
        c1.save()
        self.assertGreater(c1.updated_at, c1.created_at)
        self.assertDictEqual(
            c1.to_dict(),
            {
                'id': c1.id,
                'created_at': c1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': c1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Daniel",
                '__class__': 'City'
            }
        )

    def testNameType(self):
        """
            Check name attribute type
        """
        self.assertIsInstance(City().name, str)

    def testStateIdType(self):
        """
            Check state_id attribute type
        """
        self.assertIsInstance(City().state_id, str)


if __name__ == "__main__":
    unittest.main()
