import json

from flask import Flask, current_app, jsonify, render_template, request
from flask.views import MethodView

from project import db
from project.models.User import User


class CreateUser(MethodView):

    def post(self):
        """Create new account"""
        users_data = json.loads(request.data)
        print(users_data)
        # add new user
        name = users_data['name']
        email = users_data['email']
        password = users_data['password']
        repeat_password = users_data['repeatPassword']

        # check if user with that email exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            print("User exists")
            return jsonify({'status': 'User with that email already exists'}, 400)

        if password != repeat_password:
            return jsonify({"status": "Password doesn't match"})

        if len(password) < 6:
            return jsonify({'status': 'Password length must be 6 characters long'}, 400)

        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'New user has been added!'}, 200)

    def get(self):
        return render_template('index.html')
