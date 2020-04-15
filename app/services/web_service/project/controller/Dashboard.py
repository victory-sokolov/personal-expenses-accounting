from flask import Flask, current_app, jsonify, render_template, request
from flask.views import MethodView


class Dashboard(MethodView):

    def get(self):
        return render_template("index.html")
