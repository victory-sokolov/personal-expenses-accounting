import re
import subprocess
from subprocess import PIPE, STDOUT, Popen, check_output
from typing import Dict

from app.services.tesseract.ModelProperties import ModelProperties
from app.utils.TaskLoggerDecorator import TaskLoggerDecorator


class Evaluator:

    def __init__(self, lang: str, props: ModelProperties):
        self._lang = lang
        self.props = props(self._lang, 'model')

    def evaluate(self, default=False):
        """
        Evaluates Tesseract model for specified languages

        Parameters:
        arg1(boolean): True if need to evaluate default language model

        Returns:
        dict: result of evaluation
        """
        if default:
            model = f'{self._lang}.lstm'
            traineddata = f'{self.props.tesseract_env}/{self._lang}.traineddata'
        else:
            font_checkpoint = "hypermarket"
            model = f'{self.props.model_path}/{font_checkpoint}_checkpoint'
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
            if line.startswith('At iteration 0'):
                last_line = line

        return self.evaluated_data(last_line)

    def evaluated_data(self, eval_data: str) -> Dict:
        eval_data = eval_data.split("=")
        char_error = re.findall("\d+\.\d+", eval_data[-2])[0]
        word_error = eval_data[-1]
        return {
            'character_error': float(char_error),
            'word_error': float(word_error)
        }

    def save_evaluated_data(self):
        pass

    def plot_data(self):
        pass


evaluator = Evaluator('lav', ModelProperties)
print(evaluator.evaluate(True))
