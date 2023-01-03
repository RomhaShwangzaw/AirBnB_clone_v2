#!/usr/bin/python3
""" Unittest module for the Amenity class """


from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ Test Cases for the Amenity class """

    def testClassDocumentation(self):
        """
            Test to check Class documentation
        """
        self.assertGreater(len(Amenity.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Testing to check Constructor documentation
        """
        self.assertGreater(len(Amenity.__init__.__doc__), 0)

    def testConstructor(self):
        """
            Constructor test
        """
        a1 = Amenity()
        a1.name = "Daniel"
        a1.save()
        self.assertGreater(a1.updated_at, a1.created_at)
        self.assertDictEqual(
            a1.to_dict(),
            {
                'id': a1.id,
                'created_at': a1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': a1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'name': "Daniel",
                '__class__': 'Amenity'
            }
        )

    def testNameType(self):
        """
            Check name attribute type
        """
        self.assertIsInstance(Amenity().name, str)


if __name__ == "__main__":
    unittest.main()
