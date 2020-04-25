import os
import sys
import unittest

import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from project.controller.AddReceipt import AddReceipt
from project.controller.Authenticate import Authenticate
from project.controller.CreateUser import CreateUser
from project.controller.Dashboard import Dashboard
from project.controller.LogOutAPI import LogOutAPI
from project.controller.UserAPI import UserAPI

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    """Recreates Database"""
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database recreated")


@cli.command()
def test():
    """Run tests without code coverage"""
    print()
    tests = unittest.TestLoader().discover(
        'services/web_service/project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


# Routings
app.add_url_rule(
    '/register', view_func=CreateUser.as_view('createuser'))
app.add_url_rule('/addreceipt', view_func=AddReceipt.as_view('addreceipt'))
app.add_url_rule('/login', view_func=Authenticate.as_view('authenticate'))
app.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))
app.add_url_rule('/logout', view_func=LogOutAPI.as_view('logout'))
app.add_url_rule('/user/<id>', view_func=UserAPI.as_view('user'))


if __name__ == "__main__":
    cli()
