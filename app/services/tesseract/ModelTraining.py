import json
import os
from time import sleep
import re
import subprocess
import uuid
from subprocess import PIPE, STDOUT, Popen, check_output
from typing import Dict

from ModelProperties import ModelProperties
from OrderedClassMembers import OrderedClassMembers
from ProcessManager import ProcessManager
from utils.font import font_path
from utils.helpers import read_file, read_json
from utils.Logger import Logger


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
        sleep(2)
        process_params = [
            'lstmtraining',
            '--continue_from', f'{self._props.model_path}/{self._lang}.lstm',
            '--model_output', f'{self._props.model_path}/font',
            '--traineddata', f'{self._props.tessdata}/{self._lang}.traineddata',
            '--train_listfile', f'{self._props.training_data}/{self._lang}.training_files.txt',
            '--max_iterations', str(self._iterations)
        ]
        process = self._proc.create_process(process_params)
        self._proc.process_output(process)

    def combine(self):
        """Combine existing model with newly created."""
        Logger.info('Combining Model...', Logger.log.info)
        traineddata = f'{self._lang}-{uuid.uuid4()}.traineddata'
        process_params = [
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'{ModelProperties.model_path}/font_checkpoint',
            '--traineddata', f'{ModelProperties.tessdata}/{self._lang}.traineddata',
            '--model_output', f'{ModelProperties.model_path}/traineddata/{traineddata}'
        ]
        proc = check_output(
            process_params, text=True
        )
        # save traineddata file name
        with open('model/traineddata/traineddata.txt', 'a') as file:
            file.write(traineddata + '\n')
        return proc

    def mark_font(self):
        fonts = read_json('fonts')
        trained_fonts = ModelProperties.fonts
        for font in trained_fonts:
            fonts[font]['skip'] = True
        with open('fonts.json', 'w') as file:
            json.dump(fonts, file)
