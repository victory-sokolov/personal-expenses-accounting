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
from project.controller.UploadImage import UploadImage
from project.controller.UserAPI import UserAPI

test_dir = 'services/web_service/project/tests'

COV = coverage.Coverage(
    branch=True,
    include="/home/viktor/Documents/personal-expenses-accounting/app/services/web_service/project/*",
    omit=[
        'project/tests/*',
        'services/web_service/project/config.py'
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
    tests = unittest.TestLoader().discover(
        test_dir, pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    print(os.getcwd() + "/services/web_services/project/controller/*")
    tests = unittest.TestLoader().discover(test_dir)
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
app.add_url_rule('/upload', view_func=UploadImage.as_view('upload'))
app.add_url_rule('/login', view_func=Authenticate.as_view('authenticate'))
app.add_url_rule('/dashboard', view_func=Dashboard.as_view('dashboard'))
app.add_url_rule('/logout', view_func=LogOutAPI.as_view('logout'))
app.add_url_rule('/user/<id>', view_func=UserAPI.as_view('user'))


if __name__ == "__main__":
    cli()
