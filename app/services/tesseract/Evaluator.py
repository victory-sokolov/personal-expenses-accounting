import csv
import re
import subprocess
from subprocess import PIPE, STDOUT, Popen, check_output
from typing import Dict

from app.services.tesseract.ModelProperties import ModelProperties
from app.utils.helpers import data_to_file
from app.utils.TaskTimerDecorator import TaskTimerDecorator


class Evaluator(object):

    eval_data = None

    def __init__(self, lang: str, props: ModelProperties, default_model_eval: bool):
        self._lang = lang
        self.props = props
        self.default_model_eval = default_model_eval

    def evaluate(self):
        """Evaluates Tesseract model for specified languages."""
        if self.default_model_eval:
            model = f'{self._lang}.lstm'
            traineddata = f'{self.props.tesseract_env}/{self._lang}.traineddata'
        else:
            model = f'{self.props.model_path}/font_checkpoint'
            traineddata = f'{self.props.model_path}/{self._lang}.traineddata'

        process = subprocess.Popen([
            'lstmeval',
            '--model', model,
            '--traineddata', traineddata,
            '--eval_listfile', f'{self.props.training_data}/{self._lang}.training_files.txt'
        ], stdout=PIPE, stderr=STDOUT, text=True)

        while process.poll() is None:
            line = process.stdout.readline()
            print(line)
            if line.startswith('At iteration'):
                statistics = line
        self.eval_data = statistics

    def evaluated_data(self) -> Dict:
        """Parse string of evaluated data"""
        if self.eval_data is None:
            return 'Evaluation Failed'

        eval_data = self.eval_data.split("=")
        char_error = re.findall("\d+\.\d+", eval_data[-2])[0]
        word_error = eval_data[-1]
        self.eval_data = {
            'character_error': float(char_error),
            'word_error': float(word_error)
        }
        return self.eval_data

    def save_evaluated_data(self):
        with open('model_statistics.csv', 'w') as f:
            w = csv.DictWriter(f, self.eval_data.keys())
            w.writeheader()
            w.writerow(self.eval_data)

    def plot_data(self):
        pass
