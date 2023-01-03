#!/usr/bin/python3
"""
Unittest module for the Review Class
"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """ Test Cases for the Review class """

    def testClassDocumentation(self):
        """
            Test to check Class documentation
        """
        self.assertGreater(len(Review.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Test to check Constructor documentation
        """
        self.assertGreater(len(Review.__init__.__doc__), 0)

    def testConstructor(self):
        """
            Constructor test
        """
        r1 = Review()
        r1.text = "It's a good thing to collaborate"
        r1.save()
        self.assertGreater(r1.updated_at, r1.created_at)
        self.assertDictEqual(
            r1.to_dict(),
            {
                'id': r1.id,
                'created_at': r1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'updated_at': r1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'text': "It's a good thing to collaborate",
                '__class__': 'Review'
            }
        )

    def testPlaceIdType(self):
        """
            Check place_id type
        """
        self.assertIsInstance(Review().place_id, str)

    def testUserIdType(self):
        """
            Check user_id type
        """
        self.assertIsInstance(Review().user_id, str)

    def testTextType(self):
        """
            Check text type
        """
        self.assertIsInstance(Review().text, str)


if __name__ == "__main__":
    unittest.main()
