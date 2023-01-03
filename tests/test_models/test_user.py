#!/usr/bin/python3
"""
Unittest module for the User class
"""
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ Test Cases for the State class """

    def testClassDocumentation(self):
        """
            Test to check Class documentation
        """
        self.assertGreater(len(User.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Test to check Constructor documentation
        """
        self.assertGreater(len(User.__init__.__doc__), 0)

    def testEmailType(self):
        """
            Check email attribute type
        """
        self.assertIsInstance(User().email, str)

    def testPasswordType(self):
        """
            Check password attribute type
        """
        self.assertIsInstance(User().password, str)

    def testFirstNameType(self):
        """
            Check first_name attribute type
        """
        self.assertIsInstance(User().first_name, str)

    def testLastNameType(self):
        """
            Check last_name attribute type
        """
        self.assertIsInstance(User().last_name, str)


if __name__ == "__main__":
    unittest.main()
