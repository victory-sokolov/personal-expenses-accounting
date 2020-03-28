import create_app
import unittest
import coverage

from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    """Run tests without code coverage"""
    tests = unittests.TestLoader().discover('/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1



if __name__ == "main":
    cli()
