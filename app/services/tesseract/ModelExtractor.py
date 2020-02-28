import subprocess
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.OrderedClassMembers import OrderedClassMembers

class ModelExtractor(metaclass=OrderedClassMembers):

    def __init__(self, lang: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._props = props
        self._proc = proc

    def extract_recognition_model(self):
        process_params = [
            'combine_tessdata', '-e',
            f'{self._props.tesseract_env}/{self._lang}.traineddata',
            f'{self._lang}.lstm'
        ]
        process = self._proc.create_process(process_params)
        return process
