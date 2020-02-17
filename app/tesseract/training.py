import os
import subprocess
import sys
from subprocess import PIPE, Popen, check_output

from app.utils.font import font_path, get_fonts_names

LANG = "lav"


class MyException(Exception):
    pass


class Training:
    """Training tesseract model functions"""

    def __init__(self):
        self._langs = ['lav']
        self.TESSERACT_ENV = os.getenv("TESSDATA_PREFIX")
        self.TRAIN_FOLDER = "train_data"
        self.MODEL = "model_output"

    @property
    def langs(self):
        return self._langs

    @langs.setter
    def langs(self, langs):
        if type(langs) is not list:
            raise MyException('Argument must be list of languages')
        self._langs = langs

    def generate_training_data(self):
        max_pages = 250
        path = font_path()
        fonts = get_fonts_names()

        process = subprocess.check_output([
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', 'HypermarketW00-Light Light',
            '--lang', LANG,
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{TESSERACT_ENV}/langdata_lstm',
            '--tessdata_dir', TESSERACT_ENV,
            '--save_box_tiff',
            '--maxpages', str(max_pages),
            '--output_dir', self.TRAIN_FOLDER
        ], text=True)

        print(process)

    def evaluate(self):
        font_checkpoint = "hypermarket"

        process = subprocess.check_output([
            'lstmeval',
            '--model', f'{self.MODEL}/{font_checkpoint}_checkpoint',
            '--traineddata', f'{self.MODEL}/{LANG}.traineddata',
            '--eval_listfile', f'{self.TRAIN_FOLDER}/{LANG}.training_files.txt'
        ])

        print(process)

    def evaluate_default(self):
        process = subprocess.check_output([
            'lstmeval',
            '--model', f'{LANG}.lstm',
            '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
            '--eval_listfile', f'{self.TRAIN_FOLDER}/{LANG}.training_files.txt'
        ], text=True)

        print(process)

    def combine(self):
        checkpoint = "hypermarket"

        process = subprocess.run([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/{checkpoint}_checkpoint',
            '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
            '--model_output', f'{self.MODEL}/{LANG}.traineddata'
        ])

    def extract_recognition_model(self):
        process = subprocess.check_output([
            'combine_tessdata', '-e',
            f'{TESSERACT_ENV}/{LANG}.traineddata',
            f'{LANG}.lstm'
        ])

    def fine_tune(self):
        process = subprocess.check_output([
            'lstmtraining',
            '--continue_from', f'{LANG}.lstm',
            '--model_output', f'{self.MODEL}/hypermarket',
            '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
            '--train_listfile', f'{self.TRAIN_FOLDER}/{LANG}.training_files.txt',
            '--max_iterations', '2000'
        ], text=True)
        print(process)

    def training_pipeline(self):
        pass


# generate_training_data()
# extract_recognition_model()
# fine_tune()
# combine()
# evaluate()
train = Training()
print(train.langs)
# print(train.langs)
