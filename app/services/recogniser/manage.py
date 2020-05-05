import os
import sys
import unittest

import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from project.RecognizeAPI import RecognizeAPI

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
app.add_url_rule('/recognize', view_func=RecognizeAPI.as_view('recognize'))


if __name__ == "__main__":
    cli()
