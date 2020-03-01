import os

import cv2
import pytesseract
from PIL import Image


class Recogniser(object):

    def __init__(self, lang: str):
        self._lang = lang
        # self._props = props #props: ModelProperties

    def binarize_image(self, image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        blur_img = cv2.medianBlur(gray, 3)
        cv2.imwrite('output.png', blur_img)

    def recognise_image(self, filename):
        tessdata_dir_config = r'--tessdata-dir ""'
        config = (f'-l {self._lang} --oem 1 --psm 3')
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        return text


img = "IMG_20200123_175929.jpg"
recogniser = Recogniser("lav")
recogniser.binarise_image(img)

text = recogniser.recognise_image('output.png')
print(text)
