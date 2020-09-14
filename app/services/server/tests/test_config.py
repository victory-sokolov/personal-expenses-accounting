import os
import unittest
from pprint import pprint

from flask import current_app

from config import config
from project import create_app

class TestDevelopmentConfig(unittest.TestCase):
    """Test development config"""

    def setUp(self):
        self.app = create_app('development')

    def test_app_is_development(self):
        self.assertFalse(self.app.config['TESTING'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('SQLALCHEMY_DATABASE_URI')
        )


class TestTestingConfig(unittest.TestCase):
    """Test testing config"""

    def setUp(self):
        self.app = create_app('testing')

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('TEST_DATABASE_URL')
        )


if __name__ == '__main__':
    unittest.main()
