import datetime
import json
from functools import wraps

import jwt
from flask import Flask, current_app, g, jsonify, request
from flask_login import LoginManager
from project.models import User

EXPERATION_TIME = 2


def encode_auth_token(user_id) -> str:
    """Generates the Auth Token"""
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPERATION_TIME),
            'iat': datetime.datetime.utcnow(),
            'user_id': user_id
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """Decodes the auth token"""
    try:
        payload = jwt.decode(auth_token, current_app.config['SECRET_KEY'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        authorization = request.headers.get("Authorization")
        print(request.headers)
        if not authorization:
            return json.dumps({'status': 'no authorization token provied'}), 403, {'Content-type': 'application/json'}
        try:
            token = authorization.split(' ')[1]
            resp = decode_auth_token(token)
            print(resp['user_id'])
            current_user = User.query.filter_by(id=resp['user_id']).first()
            print(current_user)
        except:
            return json.dumps({'status': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}

        return f(current_user, *args, **kwargs)
    return wrap
