import subprocess

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.OrderedClassMembers import OrderedClassMembers
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.utils.font import (font_path, fonts_names,
                                               fonts_to_json,
                                               get_fonts_names_in_dir,
                                               supported_fonts)
from app.services.tesseract.utils.helpers import read_file, read_json

class TrainingDataGenerator(metaclass=OrderedClassMembers):

    def __init__(self, lang: str, pages: str, props: ModelProperties, proc: ProcessManager):
        self._lang = lang
        self._pages = pages
        self._props = props
        self._proc = proc

    def generate_training_data(self):
        """Generates training data"""
        path = font_path()
        fonts_to_json()
        fonts = read_json('fonts')
        #font_list = supported_fonts(get_fonts_names_in_dir(), self._lang)
        ModelProperties.fonts = supported_fonts(fonts, self._lang)
        if not self._props.fonts:
            raise ValueError('No fonts found.')

        process_params = [
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', *self._props.fonts,
            '--lang', self._lang,
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self._props.tesseract_env}/langdata_lstm',
            '--tessdata_dir', self._props.tesseract_env,
            '--save_box_tiff',
            '--maxpages', str(self._pages),
            '--output_dir', self._props.training_data
        ]
        process = self._proc.create_process(process_params)
        self._proc.process_output(process)
        return process.returncode
