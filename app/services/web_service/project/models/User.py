from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from project import db


class User(db.Model):

    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(70))
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<User name: {} \n email: {} \n password:{}>' \
            .format(self.name, self.email, self.password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def get_password(self, password):
        return check_password_hash(self.password, password)
