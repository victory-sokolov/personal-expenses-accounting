import asyncio
import os
import re
import subprocess
from subprocess import PIPE, STDOUT, Popen, check_output

from app.services.tesseract.ModelProperties import ModelProperties
from app.utils.decor import exectime
from app.utils.font import font_path
from app.utils.helpers import read_file, read_json


class ModelTraining(object):
    """Training tesseract model"""

    def __init__(self, lang: str, props: ModelProperties):
        self._lang = lang
        self._props = props

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        tesseract_langs = read_json('tesseract_langs')
        if lang in tesseract_langs:
            self._lang = lang
        else:
            raise KeyError('Language not supported')

    def extract_recognition_model(self):
        process = subprocess.call([
            'combine_tessdata', '-e',
            f'{self._props.tesseract_env}/{self._lang}.traineddata',
            f'{self._lang}.lstm'
        ])

    def fine_tune(self, iterations: int):
        process = subprocess.Popen([
            'lstmtraining',
            '--continue_from', f'{self._lang}.lstm',
            '--model_output', f'{self._props.model_path}/font',
            '--traineddata', f'{self._props.tesseract_env}/{self._lang}.traineddata',
            '--train_listfile', f'{self._props.training_data}/{self._lang}.training_files.txt',
            '--max_iterations', str(iterations)
        ], stdout=PIPE, stderr=STDOUT, text=True)

        while process.poll() is None:
            line = process.stdout.readline()
            print(line)
            if line.startswith('At iteration'):
                stats = line

        return self.get_model_statistics(stats)

    def get_model_statistics(self, stats):
        stats = stats.split("=")
        stats = list(
            filter(None, [re.findall("\d+\.\d+", stat) for stat in stats])
        )
        return {
            'Mean rms': stats[0][0],
            'delta': stats[1][0],
            'char train': stats[2][0],
            'word trian': stats[3][0],
            'worst char error': stats[4][0]
        }

    def combine(self):
        process = subprocess.call([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/font_checkpoint',
            '--traineddata', f'{self._props.tesseract_env}/{self._lang}.traineddata',
            '--model_output', f'{self._props.model_path}/{self._lang}.traineddata'
        ])
        return process
