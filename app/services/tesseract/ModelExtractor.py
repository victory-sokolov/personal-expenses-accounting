import os
import subprocess

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.OrderedClassMembers import OrderedClassMembers
from app.services.tesseract.ProcessManager import ProcessManager


class ModelExtractor(metaclass=OrderedClassMembers):

    def __init__(self, lang: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._props = props
        self._proc = proc

    def extract_recognition_model(self):
        self._props.trained_data = self._props.model_path
        # get default model on first run
        lstm_file = f'{self._props.lstm}/{self._lang}.lstm'
        if not os.path.isfile(lstm_file):
            if not os.path.exists(self._props.lstm):
                os.mkdir(self._props.lstm)
            self._props.trained_data = self._props.tesseract_env

        process_params = [
            'combine_tessdata', '-e',
            f'{self._props.trained_data}/{self._lang}.traineddata',
            f'{self._props.lstm}/{self._lang}.lstm'
        ]
        process = self._proc.create_process(process_params)
        return process.returncode
