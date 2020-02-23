from app.services.tesseract.Evaluator import Evaluator
from app.services.tesseract.ModelTraining import ModelTraining
from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator
from app.utils.TaskTimerDecorator import TaskTimerDecorator


class PipelineBuilder(object):

    def __init__(self, props):
        self._props = props

    def create_pipeline(self):
        lang = self._props.lang

        return [
            TrainingDataGenerator(lang, self._props),
            #Evaluator(lang, self._props, True)
            #ModelTraining(lang, self._props)
        ]
