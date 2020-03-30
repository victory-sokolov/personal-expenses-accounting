import os

from flask import Flask, current_app, jsonify, request, session
from flask.views import MethodView
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class AddReceipt(MethodView):

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def file_upload(self):
        target = current_app.config.get('UPLOAD_FOLDER')
        file = request.files['file']

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destination = "/".join([target, filename])
            file.save(destination)

    def post(self):
        """Get receipt data"""
        if 'file' in request.files:
            self.file_upload()

        receipt_data = request.get_json()
        print(receipt_data)
        return jsonify(receipt_data)

    def get(self):
        return 'Get Data'
