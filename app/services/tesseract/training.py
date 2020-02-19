import asyncio
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
        self.tesseract_env = os.getenv("TESSDATA_PREFIX")
        self.train_folder = "train_data"
        self.model = "model_output"

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

        # if language is supported then generate training data
        #if is_lang_supported():

        process = subprocess.call([
            'tesstrain.sh',
            '--fonts_dir', path,
            '--fontlist', 'DPix_8pt',
            '--lang', 'lav',
            '--noextract_font_properties',
            '--linedata_only',
            '--langdata_dir', f'{self.tesseract_env}/langdata_lstm',
            '--tessdata_dir', self.tesseract_env,
            '--save_box_tiff',
            '--maxpages', str(pages),
            '--output_dir', self.train_folder
        ])
        # return process

    def extract_recognition_model(self):
        process = subprocess.call([
            'combine_tessdata', '-e',
            f'{self.tesseract_env}/{LANG}.traineddata',
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
            traineddata = f'{self.tesseract_env}/{LANG}.traineddata'
        else:
            font_checkpoint = "hypermarket"
            model = f'{self.model}/{font_checkpoint}_checkpoint'
            traineddata = f'{self.model}/{LANG}.traineddata'

        process = subprocess.Popen([
            'lstmeval',
            '--model', model,
            '--traineddata', traineddata,
            '--eval_listfile', f'{self.train_folder}/{LANG}.training_files.txt'
        ], stdout=PIPE, stderr=subprocess.STDOUT, text=True)

        out = process.communicate()
        last_line = out[0].split('\n')[-2].split("=")

        char_error = re.findall("\d+\.\d+", last_line[-2])[0]
        word_error = last_line[-1]

        return {
            'character_error': float(char_error),
            'word_error': float(word_error)
        }

    def fine_tune(self, iterations):

        process = subprocess.check_output([
            'lstmtraining',
            '--continue_from', f'{LANG}.lstm',
            '--model_output', f'{self.model}/hypermarket',
            '--traineddata', f'{tesseract_env}/{LANG}.traineddata',
            '--train_listfile', f'{self.train_folder}/{LANG}.training_files.txt',
            '--max_iterations', iterations
        ], text=True)
        print(process)

    def combine(self):
        checkpoint = "hypermarket"

        process = subprocess.run([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/{checkpoint}_checkpoint',
            '--traineddata', f'{tesseract_env}/{LANG}.traineddata',
            '--model_output', f'{self.model}/{LANG}.traineddata'
        ])


    def training_pipeline(self):
        pass


train = Training()
train.generate_training_data(5)
# print(train.evaluate(True))

# train.evaluate(True)
# print(train.langs)
# print(train.langs)
