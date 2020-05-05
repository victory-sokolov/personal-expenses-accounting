import json
import unittest
from datetime import datetime

import requests

from project import create_app, db
from project.models.ReceiptData import ReceiptData
from project.models.User import User
from project.tests.base import BaseTestCase
from project.tests.utils import create_user


class TestReceipts(BaseTestCase):
    """ Test Receipts service"""

    def __init__(self, *args, **kwargs):
        self.app = create_app()
        self.app_test = self.app.test_client()
        super(TestReceipts, self).__init__(*args, **kwargs)

    def test_add_receipt(self):
        receipt_data = {
            'image': 'image_url',
            'vendor': 'SIA RIMI',
            'price': '50.00',
            'date': datetime.now(),
            'category': 'Groccery',
            'warranty': datetime(2020, 7, 12),
            'user_id': 1
        }
        response = requests.post(
            'http://localhost:5000/receipt',
            data=json.dumps(receipt_data, default=str)
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('Receipt has been added', response.json()['status'])

    def test_get_receipts_by_user_id(self):
        create_user()
        self.test_add_receipt()
        receipts = User.query.with_entities(
            User.receipts).filter_by(id=1).all()
