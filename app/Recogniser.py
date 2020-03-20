import os
import re
import subprocess

import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image

from app.services.tesseract.ProcessManager import ProcessManager


class Recogniser(object):

    def __init__(self, lang: str):
        self._lang = lang
        # self._props = props #props: ModelProperties

    def change_image_DPI(self, image):
        process_params = [
            "mogrify", "-set", "density", "300", image
        ]
        ProcessManager.create_process(process_params)

    def binarize_image(self, image):
        img = cv2.imread(image)
        kernel = np.ones((5, 5), np.uint8)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #median = cv2.medianBlur(gray, 5)
        median = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(
            median, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        #dilatate = cv2.dilate(thresh, kernel, iterations=1)
        img_erosion = cv2.erode(thresh, kernel, iterations=1)

        cv2.imwrite('output.png', thresh)

    def recognise_image(self, filename):
        tessdata_dir = r'--tessdata-dir "data/"'
        lang = []
        # with open('./traineddata/traineddata.txt', 'r') as file:
        #     lang.append(file.read().split(".")[0])

        traineddata = f'{self._lang}+eng+lav-8e87d4e0-d1a4-4543-b483-6d2535678bb4'
        black_list_chars = '#~_|!?+'

        config = (
            f'-l {traineddata} -c tessedit_char_blacklist={black_list_chars} \
            --oem 1 --psm 3 {tessdata_dir}'
        )
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        return text

    def get_date(self, text):
        date_pattern = r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$'
        text = " ".join(text).split(" ")
        for line in text:
            date = re.search(date_pattern, line)
            if date:
                return date.group(0)

    def get_vendor(self, text):
        pattern = ["SIA", "As"]
        for line in text:
            vendor = re.search(r'\bSIA|As\b', line)
            if vendor:
                return line

    def get_price(self, text):
        for line in text:
            #price = re.search(r'\bKopā\b', line)
            price = re.compile(".*(KUPĀ|KOPĀ|SUMMA){1}.*")
            if price.match(line):
                return line


image = "IMG_20200215_234244.jpg"
#image = "IMG_20200123_175929.jpg"

recogniser = Recogniser("lav")
recogniser.change_image_DPI(image)
recogniser.binarize_image(image)

output_text = list(
    filter(None, recogniser.recognise_image('output.png').split("\n"))
)

text = pytesseract.image_to_boxes(Image.open(
    'output.png'), lang='lav')


print(output_text)
# print(pytesseract.image_to_osd("result.png"))

print(recogniser.get_vendor(output_text))
print(recogniser.get_date(output_text))
print(recogniser.get_price(output_text))
