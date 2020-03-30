import os
from pathlib import Path

from flask import Flask
from flask_cors import CORS, cross_origin

from src import config


def create_app():

    app = Flask(__name__)

    # enable CORS
    CORS(app)
    os.chdir('..')
    UPLOAD_FOLDER = os.path.abspath(os.curdir) + '/recogniser'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    return app
