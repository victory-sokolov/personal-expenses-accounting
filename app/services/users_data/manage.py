import os
import unittest

import coverage
from flask.cli import FlaskGroup
from src import create_app
from src.controller.AddReceipt import AddReceipt

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    """Run tests without code coverage"""
    tests = unittest.TestLoader().discover('/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


# Routings
app.add_url_rule('/addreceipt', view_func=AddReceipt.as_view('addreceipt'))

if __name__ == "main":
    cli()
