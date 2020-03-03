import os
import re

import cv2
import numpy as np
import pytesseract
from PIL import Image


class Recogniser(object):

    def __init__(self, lang: str):
        self._lang = lang
        # self._props = props #props: ModelProperties

    def binarize_image(self, image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        cv2.imwrite('output.png', thresh)

    def recognise_image(self, filename):
        tessdata_dir_config = r'--tessdata-dir ""'
        config = (f'-l {self._lang}+"eng" --oem 1 --psm 3')
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        return text

    def get_date(self):
        output_text = recogniser.recognise_image('output.png').split("\n")

        date_pattern = r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
        for line in output_text:
            date = re.search(date_pattern, line)
            if date:
                print(date)
                return date

    def get_vendor(self):
        pattern = ["SIA", "As"]
        output_text = recogniser.recognise_image('output.png').split("\n")
        for line in output_text:
            vendor = re.search(r'\bSIA|As\b', line)
            if vendor:
                return vendor

        def get_price(self):
            pass

image = "IMG_20200123_175929.jpg"
recogniser = Recogniser("lav")
recogniser.binarize_image(image)

output_text = recogniser.recognise_image('output.png')
print(output_text)

recogniser.get_vendor()
recogniser.get_date()
