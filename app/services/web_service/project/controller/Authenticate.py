import json

from flask import Flask, current_app, jsonify, render_template, request
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash

from project import db
from project.models.User import User


class Authenticate(MethodView):

    def post(self):
        """Authenticate user"""
        users_credentials = json.loads(request.data)
        email = users_credentials['email']
        password = users_credentials['password']

        user = User.query.filter_by(email=email).first()
        validate_password = check_password_hash(user.password, password)

        if user and validate_password:
            return jsonify({'status': 'User exists'}, 200)

        return jsonify({"status": "User not found"}, 400)

    def get(self):
        return render_template('index.html')
