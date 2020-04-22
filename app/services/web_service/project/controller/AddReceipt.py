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
        """Save image"""
        file = request.files['file']
        target = current_app.config.get('UPLOAD_FOLDER')
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destination = "/".join([target, filename])
            file.save(destination)

    def save_image(self, image):
        """Convert Base64 to image and save it"""
        target = current_app.config.get('UPLOAD_FOLDER')
        date = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
        img = Image.open(BytesIO(base64.b64decode(image)))
        img.save(
            f'{target}/{date}.jpg'
        )

    def post(self):
        """Get receipt data, recognize it and save to DB"""
        # print(request.data)
        if request.data:
            if 'file' in request.files:
                self.file_upload()
            # get image in base64 format
            elif 'image' in json.loads(request.data):
                receipt_data = json.loads(request.data)
                image = receipt_data['image']
                print(image)
                self.save_image(image)

                return jsonify({'status': 'Image saved'}, 200)
            else:
                receipt_data = request.get_json()

                # if date is empty set to todays date
                if not receipt_data['date']:
                    date = datetime.date.today()
                    receipt_data['date'] = str(date)

                new_receipt = ReceiptData(
                    image=receipt_data['image'],
                    vendor=receipt_data['vendor'],
                    price=receipt_data['price'],
                    date=receipt_data['date'],
                    category='')
                db.session.add(new_receipt)
                db.session.commit()
                return jsonify({'status': 'Receipt has been added'}, 200)

        return jsonify({'status': 'Couldn\'t handle request!'}, 400)
