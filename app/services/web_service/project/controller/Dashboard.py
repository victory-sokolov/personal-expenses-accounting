from flask import Flask, current_app, jsonify, render_template, request
from flask.views import MethodView

from flask_login import login_required, current_user

class Dashboard(MethodView):
    @login_required
    def get(self):
        return render_template("index.html")
