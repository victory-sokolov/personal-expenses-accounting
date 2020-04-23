from flask import redirect, request, url_for
from flask.views import MethodView
from flask_login import logout_user


class LogOutAPI(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('authenticate'))
