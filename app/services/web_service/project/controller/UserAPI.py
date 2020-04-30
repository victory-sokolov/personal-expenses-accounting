from flask import jsonify
from flask.views import MethodView

from project.models.User import User


class UserAPI(MethodView):

    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            user_object = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'avatar': user.gravatar(),
                'receipts': user.receipts
            }
            return jsonify(user_object), 200

        return jsonify({'status': 'User not found!'}), 401
