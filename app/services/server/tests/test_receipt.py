import json
import unittest
from datetime import datetime

import requests

from config import config
from project import db, create_app
from project.models.ReceiptData import ReceiptData
from project.models.User import User
from tests.utils import user


class TestReceipts(unittest.TestCase):
    """Test Receipts service"""

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

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
        self.test_add_receipt()
        receipts = User.query.with_entities(
            User.receipts).filter_by(id=1).all()
