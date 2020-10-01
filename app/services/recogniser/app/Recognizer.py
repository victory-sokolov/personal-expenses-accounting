import json
import os
import re
from datetime import datetime
from typing import List

import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image
from redis import Redis
from rq import Queue

from app.category.search_category import SearchCategory
from app.ImageProcessing import ImageProcessing


class Recognizer(object):

    def __init__(self, lang: str):
        self._lang = lang

    def easyocr_recognize(self, filename: str) -> List:
        import easyocr

        reader = easyocr.Reader(['lv'], gpu=False)
        result = reader.readtext(filename, detail=0)

        return list(
            filter(None, result.split("\n"))
        )

    def recognise_image(self, filename) -> List:
        tessdata_dir = r'--tessdata-dir ' + f"{os.getcwd()}/app/data/"

        traineddata = f'{self._lang}+eng+lav-9bc56f04-e9fa-4046-8118-788a91cb4e92'
        black_list_chars = '#~_|!?+»=<>[]();,:*”'

        config = (
            f'-l {traineddata} -c tessedit_char_blacklist={black_list_chars} \
            --oem 1 --psm 3 {tessdata_dir}'
        )
        text = pytesseract.image_to_string(
            Image.open(filename), config=config
        )
        os.remove(f'{os.getcwd()}/app/output.png')
        return list(
            filter(None, text.split("\n"))
        )

    def get_date(self, text: List) -> str:
        date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])(-|\.)(0?[1-9]|1[012])(-|\.)([19|20]\d\d\d)'
        text = " ".join(text).split(" ")
        for line in text:
            date = re.search(date_pattern, line)
            if date:
                return date.group(0).replace(',', '.')

    def get_vendor(self, text: List) -> str:
        for line in text:
            vendor = re.search(r'\bSIA|AS\b', line)
            if vendor:
                return line
        return ""

    def get_price(self, text: List) -> str:
        for line in text:
            reg = r'.*(KUPĀ|KOPĀ|SUMMA|Samaksai).*\d+\.\s*\d{0,2}'.lower()
            if re.match(reg, line.lower()):
                price = re.findall(r'\d+\.\s*\d{0,2}', line)
                return "" if len(price) == 0 else price[0].replace(' ', '')
        return ""

    def receipt_data(self, image, user_id):
        path = f"{os.getcwd()}/app/output.png"
        # data = self.recognise_image(path)
        data = self.easyocr_recognize(path)

        vendor = self.get_vendor(data)
        date = self.get_date(data)
        price = self.get_price(data)
        category = SearchCategory(vendor).get_branch_by_shop_name()

        receipt_data = {
            'image': image.split("/")[-1],
            'vendor': vendor,
            'date': date,
            'price': price,
            'category': category,
            'user_id': user_id
        }

        requests.post(
            "http://localhost:5000/receipt",
            data=json.dumps(receipt_data),
            headers={'Content-Type': 'application/json'}
        )

    def recognise_factory(self, image, user_id):
        image_process = ImageProcessing(image)
        recognize = Recognizer("lav")

        q = Queue(connection=Redis())

        pipeline_job = q.enqueue(image_process.run_pipeline)
        q.enqueue(recognize.receipt_data, args=(
            image, user_id), depends_on=pipeline_job)

        print(
            f"Task {pipeline_job.id} added to queue at {pipeline_job.enqueued_at}. {len(q)} tasks in the queue")
