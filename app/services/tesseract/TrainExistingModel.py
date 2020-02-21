import asyncio
import os
import subprocess
from subprocess import PIPE, Popen, check_output

from app.utils.decor import exectime
from app.utils.font import font_path
from app.utils.helpers import read_file, read_json


class TrainExistingModel:
    """Training tesseract model functions"""

    def __init__(self, lang):
        self.lang = lang
        self.tesseract_env = os.getenv("TESSDATA_PREFIX")
        self.train_folder = "train_data"
        self.model = "model_output"

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        tess_lang = read_json('tesseract_langs')
        if lang in tess_lang:
            self._lang = lang
        else:
            raise KeyError('Language not supported')

    def extract_recognition_model(self):
        process = subprocess.call([
            'combine_tessdata', '-e',
            f'{self.tesseract_env}/{self._lang}.traineddata',
            f'{self._lang}.lstm'
        ])

    def fine_tune(self, iterations: int):
        process = subprocess.call([
            'lstmtraining',
            '--continue_from', f'{self._lang}.lstm',
            '--model_output', f'{self.model}/hypermarket',
            '--traineddata', f'{tesseract_env}/{self._lang}.traineddata',
            '--train_listfile', f'{self.train_folder}/{self._lang}.training_files.txt',
            '--max_iterations', iterations
        ], text=True)
        return process

    def combine(self):
        checkpoint = "hypermarket"
        process = subprocess.call([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/{checkpoint}_checkpoint',
            '--traineddata', f'{tesseract_env}/{self._lang}.traineddata',
            '--model_output', f'{self.model}/{self._lang}.traineddata'
        ])
        return process

    def instances(self, languages):
        instances = []
        for lang in languages:
            instances.append(TrainExistingModel(lang))
        return instances

    def training_pipeline(self):
        pass


train = TrainExistingModel('eng')
train.generate_training_data(5)
# print(train.evaluate(True))

# train.evaluate(True)
# print(train.langs)
# print(train.langs)
