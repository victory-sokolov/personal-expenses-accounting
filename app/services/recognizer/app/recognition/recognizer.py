import re
from typing import List
from tesserocr import OEM, PyTessBaseAPI

from .processor import ImageProcessing
from recognition.base_recognizer import Recognizer

class RecognizerProcessor(Recognizer):

    def __init__(self, lang: str):
        self._lang = lang

    def recognize(self, image = None) -> List:
        with PyTessBaseAPI(lang=f"{self._lang}+eng", oem=OEM.LSTM_ONLY) as api:
            api.SetImage(image)
            response = api.GetUTF8Text()
            return list(filter(bool,response.split(" ")))

    def get_date(self, text: List) -> str:
        date_pattern = r'^(0?[1-9]|[12][0-9]|3[01])(-|\.)(0?[1-9]|1[012])(-|\.)([19|20]\d\d\d)'
        text = " ".join(text).split(" ")
        for line in text:
            date = re.search(date_pattern, line)
            if date:
                return date.group(0).replace(',', '.')
        return ""

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

    def get_receipt_data(self, image):
        data = self.recognize(image=image)

        vendor = self.get_vendor(data)
        date = self.get_date(data)
        price = self.get_price(data)

        receipt_data = {
            'raw_data': data,
            'vendor': vendor,
            'date': date,
            'price': price
        }
        return receipt_data

    def recognize_factory(self, image):
        image_process = ImageProcessing(image)
        img = image_process.run_pipeline()
        recognizer = RecognizerProcessor(self._lang)
        data = recognizer.get_receipt_data(image=img)
        return data

