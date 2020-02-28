import os

import cv2
import pytesseract
from PIL import Image

from app.services.tesseract.ModelProperties import ModelProperties


class Recogniser(object):

    def __init__(self, lang: str, props: ModelProperties):
        self._lang = lang
        self._props = props

    def binarise_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        cv2.imwrite(image, gray)

    def recognise_image(self, filename):
        tessdata_dir_config = r'--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
        text = pytesseract.image_to_string(
            Image.open(filename), config=f'--psm 6 -l {self._lang}')
        return text

