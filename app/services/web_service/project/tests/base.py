import os
import unittest

import pytest

from project import create_app, db


class BaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.app = create_app()
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        super(BaseTestCase, self).__init__(*args, **kwargs)

    def create_app(self):
        self.app.config.from_object("project.config.TestingConfig")
        return self.app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
