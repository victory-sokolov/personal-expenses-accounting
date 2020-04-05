from flask import jsonify

from project import db


class User(db.Model):

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(70))
    password = db.Column(db.String(255))
