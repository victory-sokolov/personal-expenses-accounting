import datetime
import json

import jwt
from flask import (Flask, current_app, g, jsonify, render_template, request,
                   session)
from flask.views import MethodView
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash

from project import db
from project.auth import encode_auth_token
from project.models.User import User


class Authenticate(MethodView):

    def post(self):
        """Authenticate user"""
        user_credentials = json.loads(request.data)
        user = User.query.filter_by(email=user_credentials['email']).first()

        if user is None:
            return jsonify({'status': 'User not found'}), 401

        validate_password = check_password_hash(
            user.password, user_credentials['password'])

        if user and validate_password:
            auth_token = encode_auth_token(user.id)
            login_user(user, remember=True)
            response_object = {
                'token': auth_token.decode(),
                'id': user.id,
            }
            return jsonify(response_object), 200

        return jsonify({'status': 'Incorrect credentials'}), 401

    def get(self):
        return render_template('index.html')
