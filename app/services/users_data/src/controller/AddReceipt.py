import base64
import datetime
import json
import os
from io import BytesIO

from flask import Flask, current_app, jsonify, request, session
from flask.views import MethodView
from PIL import Image
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class AddReceipt(MethodView):

    target = current_app.config.get('UPLOAD_FOLDER')

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def file_upload(self):

        file = request.files['file']

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destination = "/".join([self.target, filename])
            file.save(destination)

    def post(self):
        """Get receipt data"""
        date = datetime.date.today()
        data = json.loads(request.data)
        img = Image.open(BytesIO(base64.b64decode(data['image'])))
        img.save(
            f'{self.target}/{date}.jpg'
        )

        if 'file' in request.files:
            self.file_upload()

        receipt_data = request.get_json()
        # if date is not recognised set todays date
        if not receipt_data['date']:
            receipt_data['date'] = date
        print(receipt_data)
        return jsonify(receipt_data)

    def get(self):
        return 'Get Data'
