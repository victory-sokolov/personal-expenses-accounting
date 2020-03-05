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
        model_path = f'{self._props.default_model_path}/{self._lang}.lstm'
        if os.path.exists(model_path):
            return

        process_params = [
            'combine_tessdata', '-e',
            f'{self._props.tesseract_env}/{self._lang}.traineddata',
            f'{model_path}'
        ]
        process = self._proc.create_process(process_params)
        return process.returncode
