import os
import subprocess

from ModelProperties import ModelProperties
from OrderedClassMembers import OrderedClassMembers
from ProcessManager import ProcessManager
from utils.Logger import Logger


class ModelExtractor(metaclass=OrderedClassMembers):

    def __init__(self, lang: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._props = props
        self._proc = proc

    def extract_recognition_model(self):
        Logger.info('Extracting recognition model...', Logger.log.info)
        process_params = [
            'combine_tessdata', '-e',
            f'{self._props.tessdata}/{self._lang}.traineddata',
            f'{self._props.model_path}/{self._lang}.lstm'
        ]
        process = self._proc.create_process(process_params)
        return process.returncode
