import base64
import datetime
import json
import os
from io import BytesIO

from flask import current_app, jsonify, request
from flask.views import MethodView
from PIL import Image
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class UploadImage(MethodView):

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
        if request.data:
            if 'file' in request.files:
                self.file_upload()
            # get image in base64 format
            elif 'image' in json.loads(request.data):
                receipt_data = json.loads(request.data)
                image = receipt_data['image']
                self.save_image(image)
                return jsonify({'status': 'Image saved'}, 200)

        return jsonify({'status': 'Couldn\'t handle request!'}, 400)
