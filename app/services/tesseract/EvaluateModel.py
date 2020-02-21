import re
import subprocess
from subprocess import PIPE, STDOUT, Popen, check_output


class EvaluateModel():

    def evaluate(self, default=False) -> dict:
        """
        Evaluates Tesseract model for specified languages

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
        ], stdout=PIPE, stderr=STDOUT, text=True)

        out = process.communicate()
        return evaluated_data(out)

    def evaluated_data(self, eval_data: str):
        out = eval_data()
        last_line = out[0].split('\n')[-2].split("=")
        char_error = re.findall("\d+\.\d+", last_line[-2])[0]
        word_error = last_line[-1]
        return {
            'character_error': float(char_error),
            'word_error': float(word_error)
        }

    def plot_data(self):
        pass


evaluate = EvaluateModel()
