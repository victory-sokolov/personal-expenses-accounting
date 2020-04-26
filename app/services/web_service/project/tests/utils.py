import requests
import json

user = {
    "name": "viktor",
    "email": "viktor@gmail.com",
    "password": "123456",
    "repeatPassword": "123456"
}


def create_user(payload=user):
    return requests.post(
        'http://localhost:5000/register', data=json.dumps(payload)
    )
