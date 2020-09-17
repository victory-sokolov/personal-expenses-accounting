import os
from pathlib import Path

from flasgger import Swagger
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app(config_name) -> object:
    app = Flask(__name__,
                static_folder="../../client",
                template_folder="../../client"
                )

    if not isinstance(config_name, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app)
    Swagger(app)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    os.chdir('..')
    UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/recogniser'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    def register_routes():
        from app.controller.Authenticate import Authenticate
        from app.controller.CreateUser import CreateUser
        from app.controller.Dashboard import Dashboard
        from app.controller.LogOutAPI import LogOutAPI
        from app.controller.ReceiptAPI import ReceiptAPI
        from app.controller.UserAPI import UserAPI

        app.add_url_rule('/register', view_func=CreateUser.as_view('register'))
        app.add_url_rule('/receipt', methods=['POST'],
                         view_func=ReceiptAPI.as_view('addreceipt'))
        app.add_url_rule(
            '/receipt/<id>', methods=['GET', 'PUT', 'DELETE'], view_func=ReceiptAPI.as_view('receipt'))
        app.add_url_rule('/login', view_func=Authenticate.as_view('login'))
        app.add_url_rule('/logout', view_func=LogOutAPI.as_view('logout'))
        app.add_url_rule(
            '/dashboard', view_func=Dashboard.as_view('dashboard'))
        app.add_url_rule('/user/<id>', view_func=UserAPI.as_view('user'))

    register_routes()
    return app
