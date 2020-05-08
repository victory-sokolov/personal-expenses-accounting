import base64
import datetime
import json
import os
from io import BytesIO

from flask import current_app, g, jsonify, request
from flask.views import MethodView
from PIL import Image
from werkzeug.utils import secure_filename

from project.Recognizer import Recognizer

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class RecognizeAPI(MethodView):

    def allowed_files(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def file_upload(self):
        """Save image"""
        file = request.files['file']
        target = current_app.config.get('UPLOAD_FOLDER')
        if file and self.allowed_files(file.filename):
            filename = secure_filename(file.filename)
            destination = "/".join([target, filename])
            file.save(destination)

    def imageToBase64(self, image) -> str:
        """Convert Base64 to image and return its name"""
        target = current_app.config.get('UPLOAD_FOLDER')
        date = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
        base64_to_image = Image.open(BytesIO(base64.b64decode(image)))
        image_path = f'{target}/{date}.jpg'
        base64_to_image.save(image_path)
        return image_path

    def post(self):
        if request.data:
            if 'file' in request.files:
                self.file_upload()
            # get image in base64 format
            elif 'image' in json.loads(request.data):
                receipt_data = json.loads(request.data)
                base64_image = receipt_data['image']
                user_id = receipt_data['id']
                image = self.imageToBase64(base64_image)
                Recognizer('lav').recognise_factory(image, user_id)
                return jsonify({'status': 'Image Recognized'}), 200

        return jsonify({'status': 'Cannot handle request!'}), 400
