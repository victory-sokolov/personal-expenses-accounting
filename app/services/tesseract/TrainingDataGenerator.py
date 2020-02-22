import subprocess

from app.services.tesseract.ModelProperties import ModelProperties
from app.utils.font import font_path, get_fonts_names, supported_fonts
from app.utils.helpers import read_file
from app.utils.TaskLoggerDecorator import TaskLoggerDecorator


class TrainingDataGenerator(object):

    def __init__(self, lang: str, props: ModelProperties):
        self._lang = lang
        self.props = props(self._lang, 'model')

    def generate_training_data(self, pages=250):
        """Generates training data"""
        path = font_path()
        font_list = supported_fonts(get_fonts_names(), self._lang)
        print(font_list)

        process = subprocess.call([
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', *font_list,
            '--lang', self._lang,
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self.props.tesseract_env}/langdata_lstm',
            '--tessdata_dir', self.props.tesseract_env,
            '--save_box_tiff',
            '--maxpages', str(pages),
            '--output_dir', self.props.training_data
        ])

        return process


train = TrainingDataGenerator('lav', ModelProperties)
train.generate_training_data(5)
# log = TaskLoggerDecorator(TrainingDataGenerator('lav', ModelProperties))
# print(log)
