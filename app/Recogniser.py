import os

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


image = "IMG_20200123_175929.jpg"
recogniser = Recogniser("lav")
recogniser.binarize_image(image)

output_text = recogniser.recognise_image('output.png')
print(output_text)
