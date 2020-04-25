import json
import unittest

import requests

from project import create_app, db
from project.models import User
from project.tests.base import BaseTestCase


class TestUsers(BaseTestCase):
    """ Test Users service"""

    def __init__(self, *args, **kwargs):
        self.app = create_app()
        self.app_test = self.app.test_client()
        super(TestUsers, self).__init__(*args, **kwargs)

    def test_add_user(self):
        """Ensure user is added to db"""
        payload = {
            "name": "viktor",
            "email": "viktor@gmail.com",
            "password": "123456",
            "repeatPassword": "123456"
        }

        response = requests.post(
            'http://localhost:5000/register', data=json.dumps(payload))
        print(response.text)
        self.assertEqual(response.status_code, 200)

    def test_add_dublicate_email(self):
        pass

    def test_get_single_user(self):
        pass

    def test_get_all_users(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
