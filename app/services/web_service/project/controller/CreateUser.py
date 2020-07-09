import json

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask.views import MethodView
from flask_login import current_user, login_required

from project import db
from project.auth import encode_auth_token
from project.models.User import User


class CreateUser(MethodView):
    def post(self):
        """Create new account"""
        user_data = json.loads(request.data)

        user_exists = User.query.filter_by(email=user_data["email"]).first()
        if user_exists:
            return jsonify({"status": "User with that email already exists"}), 400

        if user_data["password"] != user_data["repeatPassword"]:
            return jsonify({"status": "Password doesn't match"}), 400

        if len(user_data["password"]) < 6:
            return jsonify({"status": "Password length must be 6 characters long"}), 400

        user = User(name=user_data["name"], email=user_data["email"],)
        user.set_password(user_data["password"])
        user.gravatar()
        db.session.add(user)
        db.session.commit()
        # confirm email
        # token = User.generate_confirmation_token(user_data['email'])
        # send_email(user_data['email'], 'Confirm Your Account',
        #            'email/confirm', user=user, token=token)

        auth_token = encode_auth_token(user.id)
        response = {
            "status": "success",
            "message": "Successfully registered.",
            "auth_token": auth_token.decode(),
        }
        return jsonify(response), 200

    def get(self):
        return render_template("index.html"), 200

    @login_required
    def confirm_email(self, token):
        if current_user.confirmed:
            return redirect(url_for("main.index"))
        if current_user.confirm(token):
            db.session.commit()
            flash("You have confirmed your account. Thanks!")
        else:
            flash("The confirmation link is invalid or has expired.")
        return redirect(url_for("main.index"))
