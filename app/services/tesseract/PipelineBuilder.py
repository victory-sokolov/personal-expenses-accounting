from app.services.tesseract.Evaluator import Evaluator
from app.services.tesseract.ModelExtractor import ModelExtractor
from app.services.tesseract.ModelTraining import ModelTraining
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator


class PipelineBuilder(object):

    def __init__(self, props):
        self._props = props

    def create_pipeline(self):
        lang = self._props.lang
        self._props.init_setup()
        return [
            TrainingDataGenerator(lang, self._props, ProcessManager),
            ModelExtractor(lang, self._props, ProcessManager),
            Evaluator(lang, self._props, ProcessManager, True),
            ModelTraining(lang, self._props, ProcessManager),
            Evaluator(lang, self._props, ProcessManager, False)
        ]
