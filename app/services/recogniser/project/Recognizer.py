import json
import os
import re
from time import sleep

import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image

from project.ImageProcessing import ImageProcessing


class Recogniser(object):

    def __init__(self, lang: str):
        self._lang = lang

    def recognise_image(self, filename):
        tessdata_dir = r'--tessdata-dir "recogniser/project/data/"'

        traineddata = f'{self._lang}+eng+lav-9bc56f04-e9fa-4046-8118-788a91cb4e92'
        black_list_chars = '#~_|!?+»=<>[]();,:*”'

        config = (
            f'-l {traineddata} -c tessedit_char_blacklist={black_list_chars} \
            --oem 1 --psm 3 {tessdata_dir}'
        )
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        os.remove('recogniser/project/output.png')
        return list(
            filter(None, text.split("\n"))
        )

    def get_date(self, text):
        date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])(-|\.)(0?[1-9]|1[012])(-|\.)([19|20]\d\d\d)'
        text = " ".join(text).split(" ")
        for line in text:
            date = re.search(date_pattern, line)
            if date:
                return date.group(0).replace(',', '.')

    def get_vendor(self, text):
        for line in text:
            vendor = re.search(r'\bSIA|As\b', line)
            if vendor:
                return line

    def get_price(self, text):
        for line in text:
            price = re.compile(".*(KUPĀ|KOPĀ|SUMMA){1}.*")
            if price.match(line):
                price = re.findall(r'\d+\.\d{2}', line)[0]
                return price

    def receipt_data(self, image, user_id):
        data = self.recognise_image('recogniser/project/output.png')
        vendor = self.get_vendor(data)
        date = self.get_date(data)
        price = self.get_price(data)
        receipt_data = {
            'image': image,
            'vendor': vendor,
            'date': date,
            'price': price,
            'user_id': user_id
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(
            "http://localhost:5000/addreceipt",
            data=json.dumps(receipt_data),
            headers=headers
        )


def recognise_factory(image, user_id):
    ImageProcessing(image).run_pipeline()
    Recogniser("lav").receipt_data(image, user_id)


recognise_factory('2020-05-01-18-12-24.jpg', 1)
