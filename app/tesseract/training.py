import os
import re
import subprocess
import sys
from subprocess import PIPE, Popen, check_output

from app.utils.decor import exectime
from app.utils.font import font_path
from app.utils.helpers import read_file

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

    def generate_training_data(self, pages=250):
        """Generates training data"""
        path = font_path()
        font_list = read_file('fonts.txt')

        process = subprocess.call([
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', 'DPix_8pt',
            '--lang', 'eng',
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self.TESSERACT_ENV}/langdata_lstm',
            '--tessdata_dir', self.TESSERACT_ENV,
            '--save_box_tiff',
            '--maxpages', str(pages),
            '--output_dir', self.TRAIN_FOLDER
        ])
        # return process

    def extract_recognition_model(self):
        process = subprocess.call([
            'combine_tessdata', '-e',
            f'{self.TESSERACT_ENV}/{LANG}.traineddata',
            f'{LANG}.lstm'
        ])

    def evaluate(self, default=False):
        """
        Evaluates default Tesseract models for specified languages

        Parameters:
        arg1(boolean): True if need to evaluate default language model

        Returns:
        dict: result of evaluation
        """
        if default:
            model = f'{LANG}.lstm'
            traineddata = f'{self.TESSERACT_ENV}/{LANG}.traineddata'
        else:
            font_checkpoint = "hypermarket"
            model = f'{self.MODEL}/{font_checkpoint}_checkpoint'
            traineddata = f'{self.MODEL}/{LANG}.traineddata'

        process = subprocess.Popen([
            'lstmeval',
            '--model', model,
            '--traineddata', traineddata,
            '--eval_listfile', f'{self.TRAIN_FOLDER}/{LANG}.training_files.txt'
        ], stdout=PIPE, stderr=subprocess.STDOUT, text=True)

        out = process.communicate()
        last_line = out[0].split('\n')[-2].split("=")

        char_error = re.findall("\d+\.\d+", last_line[-2])[0]
        word_error = last_line[-1]

        return {
            'character_error': float(char_error),
            'word_error': float(word_error)
        }

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

    def combine(self):
        checkpoint = "hypermarket"

        process = subprocess.run([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/{checkpoint}_checkpoint',
            '--traineddata', f'{TESSERACT_ENV}/{LANG}.traineddata',
            '--model_output', f'{self.MODEL}/{LANG}.traineddata'
        ])

    def training_pipeline(self):
        pass


# extract_recognition_model()
# fine_tune()
# combine()
# evaluate()
train = Training()
train.generate_training_data(5)
# print(train.evaluate(True))

# train.evaluate(True)
# print(train.langs)
# print(train.langs)
