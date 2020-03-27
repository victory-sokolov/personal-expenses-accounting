import os
import re
import subprocess

import cv2
import numpy as np
import pytesseract
from PIL import Image

from ImageProcessing import ImageProcessing
from services.tesseract.ProcessManager import ProcessManager


class Recogniser(object):

    def __init__(self, lang: str):
        self._lang = lang

    def recognise_image(self, filename):
        tessdata_dir = r'--tessdata-dir "data/"'

        traineddata = f'{self._lang}+eng+lav-9bc56f04-e9fa-4046-8118-788a91cb4e92'
        black_list_chars = '#~_|!?+»=<>[]();,:*'

        config = (
            f'-l {traineddata} -c tessedit_char_blacklist={black_list_chars} \
            --oem 1 --psm 3 {tessdata_dir}'
        )
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        os.remove('output.png')
        return list(
            filter(None, text.split("\n"))
        )

    def get_date(self, text):
        date_pattern = r'^([0-9]{2,4}(\.|-)[0-9]{2}(\.|-)[0-9]{2,4})'
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

    def return_receitps_as_dict(self):
        data = self.recognise_image('output.png')
        vendor = self.get_vendor(data)
        date = self.get_date(data)
        price = self.get_price(data)
        return {
            'vendor': vendor,
            'date': date,
            'price': price
        }


image = "IMG_20200215_234244.jpg"

ImageProcessing().run_pipeline(image)
recogniser = Recogniser("lav")

print(recogniser.return_receitps_as_dict())
