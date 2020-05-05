import os
from pathlib import Path

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app():
    app = Flask(__name__,
                static_folder="../../client",
                template_folder="../../client")

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    os.chdir('..')
    UPLOAD_FOLDER = os.path.abspath(
        os.curdir) + '/recogniser/project/receipts'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
