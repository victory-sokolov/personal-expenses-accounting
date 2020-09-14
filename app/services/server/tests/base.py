import os
import unittest

import pytest

from config import config
from project import create_app, db

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
