import subprocess

from app.services.tesseract.ModelProperties import ModelProperties
from app.utils.font import (font_path, fonts_names, get_font_names,
                            get_fonts_names_in_dir, supported_fonts)
from app.utils.helpers import read_file
from app.utils.TaskTimerDecorator import TaskTimerDecorator


class TrainingDataGenerator(object):

    def __init__(self, lang: str, props: ModelProperties):
        self._lang = lang
        self._props = props

    def generate_training_data(self):
        """Generates training data"""
        path = font_path()
        font_list = supported_fonts(get_fonts_names_in_dir(), self._lang)

        process = subprocess.call([
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', *font_list,
            '--lang', self._lang,
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self._props.tesseract_env}/langdata_lstm',
            '--tessdata_dir', self._props.tesseract_env,
            '--save_box_tiff',
            '--maxpages', str(self._props.pages),
            '--output_dir', self._props.training_data
        ])

        return process
