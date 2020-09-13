import os
import sys
import unittest

import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from project.models import ReceiptData, User


COV = coverage.Coverage(
    branch=True,
    include="app/*",
    omit=[
        'project/tests/*',
        'services/web_service/config.py'
    ]
)
COV.start()

config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)
cli = FlaskGroup(create_app=create_app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, ReceiptData=ReceiptData)


@cli.command("recreate_db")
def recreate_db():
    """Recreates Database"""
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Database recreated")


@cli.command()
def tests():
    """Run tests without code coverage"""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover()
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


if __name__ == "__main__":
    cli()
