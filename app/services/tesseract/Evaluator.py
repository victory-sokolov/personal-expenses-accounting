import csv
import os
import re
from typing import Dict

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.OrderedClassMembers import OrderedClassMembers
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.utils.helpers import data_to_file
from app.services.tesseract.utils.TaskTimerDecorator import TaskTimerDecorator


class Evaluator(metaclass=OrderedClassMembers):

    eval_data = []
    file_prefix = None

    def __init__(self, lang: str, props: ModelProperties, proc: ProcessManager, default_model_eval: bool):
        self._lang = lang
        self._props = props
        self.default_model_eval = default_model_eval
        self._proc = proc

    def evaluate(self):
        """Evaluates Tesseract model for specified languages."""
        if self.default_model_eval:
            model = f'{self._props.lstm}/{self._lang}.lstm'
            self.file_prefix = "before"
        else:
            model = f'{self._props.model_path}/font_checkpoint'
            self.file_prefix = "after"

        training_file = f'{self._props.training_data}/{self._lang}.training_files.txt'

        if os.path.exists(training_file):
            with open(training_file) as file:
                for lstmf in file:
                    with open('training.txt', 'w') as fs:
                        fs.write(lstmf)

                    process_params = [
                        'lstmeval',
                        '--model', model,
                        '--traineddata', f'{self._props.trained_data}/{self._lang}.traineddata',
                        '--eval_listfile', 'training.txt'
                    ]
                    process = self._proc.create_process(process_params)
                    statistics = self._proc.process_output(process)

                    os.remove('training.txt')
                    font = re.split("[/,.]", lstmf)[-3]
                    self.eval_data.append(
                        {'font': font, 'statistics': statistics}
                    )

    def evaluated_data(self) -> Dict:
        """Parse string of evaluated data"""
        if not self.eval_data:
            return 'Evaluation Failed'

        statistics = [stat['statistics'] for stat in self.eval_data]

        for count, stat in enumerate(statistics):
            eval_data = stat.split("=")
            char_error = re.findall(r"\d+\.\d+", eval_data[-2])[0]
            word_error = eval_data[-1]

            self.eval_data[count]['character_error'] = float(char_error)
            self.eval_data[count]['word_error'] = float(word_error)
            del self.eval_data[count]['statistics']

        return self.eval_data

    def save_evaluated_data(self):
        file = f'{self._props.stats}/{self.file_prefix}_{self._lang}_model_statistics.csv'
        file_exists = os.path.isfile(file)
        if self.eval_data:
            with open(file, 'a') as data:
                write = csv.DictWriter(
                    data, fieldnames=self.eval_data[0].keys()
                )
                if not file_exists:
                    write.writeheader()
                write.writerows(self.eval_data)
            del self.eval_data[:]
