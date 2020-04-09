import os
import unittest

import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from project.controller.AddReceipt import AddReceipt
from project.controller.Authenticate import Authenticate
from project.controller.CreateUser import CreateUser

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


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# Routings
app.add_url_rule(
    '/register', view_func=CreateUser.as_view('createuser'))
app.add_url_rule('/addreceipt', view_func=AddReceipt.as_view('addreceipt'))
app.add_url_rule('/login', view_func=Authenticate.as_view('authenticate'))


if __name__ == "main":
    cli()
