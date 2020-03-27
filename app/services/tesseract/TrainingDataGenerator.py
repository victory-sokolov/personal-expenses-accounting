import subprocess

from ModelProperties import ModelProperties
from OrderedClassMembers import OrderedClassMembers
from ProcessManager import ProcessManager
from utils.font import fonts_to_json, supported_fonts
from utils.helpers import read_file, read_json


class TrainingDataGenerator(metaclass=OrderedClassMembers):

    def __init__(self, lang: str, pages: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._pages = pages
        self._props = props
        self._proc = proc

    def generate_training_data(self):
        """Generates training data"""
        path = './fonts/'
        fonts_to_json()
        fonts = read_json('fonts')
        ModelProperties.fonts = supported_fonts(fonts, self._lang)
        # skip to next language
        if not self._props.fonts:
            print(f'No supported fonts found for {self._lang} language')

        process_params = [
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', *self._props.fonts,
            '--lang', self._lang,
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self._props.tessdata}/langdata_lstm',
            '--tessdata_dir', self._props.tessdata,
            '--save_box_tiff',
            '--maxpages', str(self._pages),
            '--output_dir', self._props.training_data
        ]
        process = self._proc.create_process(process_params)
        self._proc.process_output(process)
        return process.returncode
