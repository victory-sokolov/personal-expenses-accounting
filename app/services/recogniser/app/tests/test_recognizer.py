import unittest
from datetime import datetime

import pytest
import requests
from parameterized import parameterized

from project import create_app
from project.Recognizer import Recognizer
from project.tests.base import BaseTestCase


class TestRecognizer(BaseTestCase):
    """ Test Recognizer service"""

    params = {
        "test_get_price": [dict(input='Kopa EUR 19.00', expected='19.00')],
    }

    def __init__(self, *args, **kwargs):
        self.app = create_app()
        self.app_test = self.app.test_client()
        self.recognizer = Recognizer('lav')
        super(TestRecognizer, self).__init__(*args, **kwargs)

    @parameterized.expand([
        (['KOPĀ EUR 19.00'], '19.00'),
        (['KUPĀ EUR  19.20'], '19.20'),
        (['KOPĀ EUR  119.0'], '119.0'),
        (['Samaksai EUR  5.00'], '5.00'),
        (['Kopā EUR  5.00'], '5.00'),
    ])
    def test_get_price(self, test_input, expected):
        """ Test price extraction"""
        price = self.recognizer.get_price(test_input)
        self.assertEqual(price, expected)

    @parameterized.expand([
        (['SIA RIMI'], 'SIA RIMI'),
        (['AS Balticom'], 'AS Balticom'),
    ])
    def test_get_vendor(self, test_input, expected):
        """Test vendor extraction"""
        vendor = self.recognizer.get_vendor(test_input)
        self.assertEqual(vendor, expected)
        self.assertNotEqual(vendor, 'IAS')

    @parameterized.expand([
        (['2020.5.17'], '2020.5.17'),
    ])
    def test_get_date(self, test_input, expected):
        date = self.recognizer.get_date(test_input)
        self.assertEqual(date, expected)
