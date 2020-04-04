import os
from pathlib import Path

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from project import config

db = SQLAlchemy()
migrate = Migrate()

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    os.chdir('..')
    UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/recogniser'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
