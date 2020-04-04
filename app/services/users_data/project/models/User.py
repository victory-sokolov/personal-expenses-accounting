from flask import jsonify

from project import db


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(70))

    def create_user(self, user):
        name = user['name']
        email = user['email']
        create_user = User(name, email)
        db.session.add(create_user)
        db.session.commit()

        if create_user:
            return jsonify({'status': 'New user has benn added!'}, 200)
        return jsonify({'status': 'Failed to add user'}, 400)

    def update_user_by_id(self, id):
        pass
