import base64
import datetime
import json
import os
from io import BytesIO

from flask import Flask, current_app, jsonify, request, session
from flask.views import MethodView
from PIL import Image
from werkzeug.utils import secure_filename

from project import db
from project.models.ReceiptData import ReceiptData

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class AddReceipt(MethodView):

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def file_upload(self):
        file = request.files['file']
        target = current_app.config.get('UPLOAD_FOLDER')
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destination = "/".join([target, filename])
            file.save(destination)

    def post(self):
        """Get receipt data"""
        if 'file' in request.files:
            self.file_upload()
        # get image in base64 format
        elif 'image' in json.loads(request.data):
            target = current_app.config.get('UPLOAD_FOLDER')
            date = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
            data = json.loads(request.data)
            img = Image.open(BytesIO(base64.b64decode(data['image'])))
            img.save(
                f'{target}/{date}.jpg'
            )
            return jsonify({'status': 200})
        else:
            receipt_data = request.get_json()
            date = datetime.date.today()
            if not receipt_data['date']:
                receipt_data['date'] = str(date)

            # add receipt to DB
            vendor = receipt_data['vendor']
            price = receipt_data['price']
            date = receipt_data['date']
            category = receipt_data['category']

            new_receipt = ReceiptData(vendor=vendor, price=price, date=date, category=category)
            db.session.add(new_receipt)
            db.session.commit()
            return jsonify({'status': 'Receipt has been added'}, 200)

        return jsonify({'status': 'Couldn\'t handle image!'}, 400)
