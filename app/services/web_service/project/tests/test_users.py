import json
import unittest

import requests

from project import create_app, db
from project.models.User import User
from project.tests.base import BaseTestCase
from utils import create_user


class TestUsers(BaseTestCase):
    """ Test Users service"""

    def __init__(self, *args, **kwargs):
        self.app = create_app()
        self.app_test = self.app.test_client()

        super(TestUsers, self).__init__(*args, **kwargs)

    def test_add_user(self):
        """Ensure user is added to db"""
        response = create_user()
        self.assertIn("success", response.json()['status'])
        self.assertEqual(response.status_code, 200)

    def test_add_dublicate_email(self):
        self.test_add_user()
        response = create_user()
        self.assertIn("User with that email already exists",
                      response.json()['status']
                      )
        self.assertEqual(response.status_code, 400)

    def test_password_length(self):
        payload = {
            "name": "viktor",
            "email": "viktor@gmail.com",
            "password": "12345",
            "repeatPassword": "12345"
        }
        response = create_user(payload)
        self.assertIn("Password length must be 6 characters long",
                      response.json()['status']
                      )
        self.assertEqual(response.status_code, 400)

    def test_get_user_by_id(self):
        user = User(name="viktor",
                    email="viktorsokolov.and@gmail.com", password="123456")
        db.session.add(user)
        db.session.commit()
        response = requests.get(f'http://localhost:5000/user/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('viktor', response.json()['name'])

    def test_get_all_users(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
