import json

from flask import jsonify
from flask.views import MethodView

from flasgger import swag_from
from project.models.User import User


class UserAPI(MethodView):

    @swag_from('UserAPI.yml')
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        receipts = []

        if user:

            for receipt in user.receipts:
                dictret = dict(receipt.__dict__)
                dictret.pop('_sa_instance_state', None)
                receipts.append(dictret)

            user_object = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'avatar': user.gravatar(),
                'receipts': receipts
            }

            return jsonify(user_object), 200

        return jsonify({'status': 'User not found!'}), 401
