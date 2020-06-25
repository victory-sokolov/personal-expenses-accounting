import os
import unittest
from pprint import pprint

from flask import current_app

from config import config
from project import create_app
from project.tests.base import BaseTestCase


class TestDevelopmentConfig(BaseTestCase):
    """Test development config"""

    def __init__(self, *args, **kwargs):
        self.app = create_app('development')
        self.app.config.from_object(config['development'])
        super(TestDevelopmentConfig, self).__init__(*args, **kwargs)

    def test_app_is_development(self):
        self.assertFalse(self.app.config['TESTING'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('SQLALCHEMY_DATABASE_URI')
        )


class TestTestingConfig(BaseTestCase):
    """Test testing config"""

    def __init__(self, *args, **kwargs):
        self.app = create_app('testing')
        super(TestTestingConfig, self).__init__(*args, **kwargs)

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] ==
            os.environ.get('TEST_DATABASE_URL')
        )
