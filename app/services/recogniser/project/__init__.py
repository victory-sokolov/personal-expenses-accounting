import os
from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from config import config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app(config_name) -> object:
    app = Flask(__name__,
                static_folder="../../client",
                template_folder="../../client")

    if not isinstance(config_name, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
