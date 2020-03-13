import json
import os
import re
import subprocess
from subprocess import PIPE, STDOUT, Popen, check_output
from typing import Dict

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.OrderedClassMembers import OrderedClassMembers
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.utils.font import font_path
from app.services.tesseract.utils.helpers import read_file, read_json
from app.services.tesseract.utils.Logger import Logger


class ModelTraining(metaclass=OrderedClassMembers):
    """Training tesseract model"""

    def __init__(self, lang: str, iterations: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._iterations = iterations
        self._props = props
        self._proc = proc

    @property
    def lang(self) -> str:
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        tesseract_langs = read_json('utils/tesseract_langs')
        if lang in tesseract_langs:
            self._lang = lang
        else:
            raise KeyError('Language not supported')

    def fine_tune(self):
        Logger.info('Finetuning Model...', Logger.log.info)

        process_params = [
            'lstmtraining',
            '--continue_from', f'{ModelProperties.lstm}/{self._lang}.lstm',
            '--model_output', f'{ModelProperties.model_path}/font',
            '--traineddata', f'{ModelProperties.trained_data}/{self._lang}.traineddata',
            '--train_listfile', f'{ModelProperties.training_data}/{self._lang}.training_files.txt',
            '--max_iterations', str(self._iterations)
        ]
        process = self._proc.create_process(process_params)
        self._proc.process_output(process)

    def combine(self):
        """Combine existing model with newly created."""
        Logger.info('Combining Model...', Logger.log.info)
        #model_output = f'{ModelProperties.model_path}/{self._lang}.traineddata'
        process_params = [
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'{ModelProperties.model_path}/font_checkpoint',
            '--traineddata', f'{ModelProperties.trained_data}/{self._lang}.traineddata',
            '--model_output', f'./{self._lang}.traineddata'
        ]
        proc = check_output(
            process_params, text=True
        )
        return proc

    def mark_font(self):
        fonts = read_json('fonts')
        trained_fonts = ModelProperties.fonts

        for font in trained_fonts:
            fonts[font]['skip'] = True
        # write data
        with open('fonts.json', 'w') as file:
            json.dump(fonts, file)
