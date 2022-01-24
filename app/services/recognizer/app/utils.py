import base64
import datetime
import io

import numpy as np
import cv2
from io import BytesIO
from PIL import Image

from config import settings

def allowed_files(filename):
    extension = settings.ALLOWED_IMAGE_EXTENSIONS
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extension


def base64_data_to_image(image: str) -> str:
    """Convert Base64 to image and return its name"""
    target = settings.UPLOAD_FOLDER
    date = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
    base64_to_image = Image.open(BytesIO(base64.b64decode(image)))
    image_path = f'{target}/{date}.jpg'
    base64_to_image.save(image_path)
    return image_path

def string_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))

def to_RGB(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
