from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)


class AddReceipt(MethodView):

    def post(self):
        """Get receipt data"""
        receipt_data = request.get_json()
        return

    def get(self):
        return 'Get Data'


app.add_url_rule('/addreceipt', view_func=AddReceipt.as_view('addreceipt'))
