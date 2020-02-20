import asyncio
import os
import re
import subprocess
import sys
from subprocess import PIPE, Popen, check_output

from app.utils.decor import exectime
from app.utils.font import font_path, is_lang_supported
from app.utils.helpers import read_file, read_json


class TrainingModel:
    """Training tesseract model functions"""

    def __init__(self, lang):
        self.lang = lang
        self.tesseract_env = os.getenv("TESSDATA_PREFIX")
        self.train_folder = "train_data"
        self.model = "model_output"

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        tess_lang = read_json('tesseract_langs')
        if lang in tess_lang:
            self._lang = lang
        else:
            raise KeyError('Language not supported')

    def generate_training_data(self, pages=250):
        """Generates training data"""
        path = font_path()
        font_list = read_file('fonts.txt')

        # if language is supported then generate training data
        font = 'OCR-A'
        if is_lang_supported(font, self.lang):
            process = subprocess.call([
                'tesstrain.sh',
                '--fonts_dir', path,
                '--fontlist', 'OCR-A',
                '--lang', self.lang,
                '--noextract_font_properties',
                '--linedata_only',
                '--langdata_dir', f'{self.tesseract_env}/langdata_lstm',
                '--tessdata_dir', self.tesseract_env,
                '--save_box_tiff',
                '--maxpages', str(pages),
                '--output_dir', self.train_folder
            ])
        else:
            print(f"Font {font} doesn't support {self.lang} language")
        # return process

    def extract_recognition_model(self):
        process = subprocess.call([
            'combine_tessdata', '-e',
            f'{self.tesseract_env}/{self._lang}.traineddata',
            f'{self._lang}.lstm'
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
            model = f'{self._lang}.lstm'
            traineddata = f'{self.tesseract_env}/{self._lang}.traineddata'
        else:
            font_checkpoint = "hypermarket"
            model = f'{self.model}/{font_checkpoint}_checkpoint'
            traineddata = f'{self.model}/{self._lang}.traineddata'

        process = subprocess.Popen([
            'lstmeval',
            '--model', model,
            '--traineddata', traineddata,
            '--eval_listfile', f'{self.train_folder}/{self._lang}.training_files.txt'
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
            '--continue_from', f'{self._lang}.lstm',
            '--model_output', f'{self.model}/hypermarket',
            '--traineddata', f'{tesseract_env}/{self._lang}.traineddata',
            '--train_listfile', f'{self.train_folder}/{self._lang}.training_files.txt',
            '--max_iterations', iterations
        ], text=True)
        print(process)

    def combine(self):
        checkpoint = "hypermarket"

        process = subprocess.run([
            'lstmtraining',
            '--stop_training',
            '--continue_from', f'model_output/{checkpoint}_checkpoint',
            '--traineddata', f'{tesseract_env}/{self._lang}.traineddata',
            '--model_output', f'{self.model}/{self._lang}.traineddata'
        ])

    def instances(self, languages):
        instances = []
        for lang in languages:
            instances.append(TrainingModel(lang))
        return instances

    def training_pipeline(self):
        pass


train = TrainingModel('eng')
train.generate_training_data(5)
# print(train.evaluate(True))

# train.evaluate(True)
# print(train.langs)
# print(train.langs)
