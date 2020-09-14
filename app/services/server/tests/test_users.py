import json
import unittest

import requests

from project import create_app, db
from project.models.User import User
from tests.utils import user


class TestUsers(unittest.TestCase):
    """ Test Users service"""

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self):
        return {
            "Authorization": "Basic ",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def test_add_user(self):
        """Ensure user is added to db"""
        # user = {
        #     "name": "viktor",
        #     "email": "viktor@gmail.com",
        #     "password": "123456",
        #     "repeatPassword": "123456",
        # }
        response = self.client.post(
            "/register", headers=self.get_api_headers(), data=json.dumps(user)
        )
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIn("success", json_response["status"])
        self.assertEqual(response.status_code, 200)

    def test_add_dublicate_email(self):
        response = self.test_add_user()
        # response = self.client.post(
        #     "/register", header=self.get_api_headers(), data=json.dumps(user)
        # )
        json_response = json.loads(response.get_data(as_text=True))
        self.assertIn("User with that email already exists",
                      json_response['status'])
        self.assertEqual(response.status_code, 400)

    # def test_password_length(self):
    #     payload = {
    #         "name": "viktor",
    #         "email": "viktor@gmail.com",
    #         "password": "12345",
    #         "repeatPassword": "12345"
    #     }
    #     response = create_user(payload)
    #     print(response)
    #     self.assertIn("Password length must be 6 characters long",
    #                   response.json()['status']
    #                   )
    #     self.assertEqual(response.status_code, 400)

    def test_get_user_by_id(self):
        user = User(name="viktor",
                    email="viktorsokolov.and@gmail.com", password="123456")
        db.session.add(user)
        db.session.commit()
        response = self.client.get(f'/user/{user.id}')
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn('viktor', json_response['name'])


if __name__ == "__main__":
    unittest.main()
