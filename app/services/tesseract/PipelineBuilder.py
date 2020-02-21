from app.services.tesseract import (Evaluator,
                                    ModelTrainer,
                                    TrainingDataGenerator)
from app.utils import TaskLoggerDecorator


class PipelineBuilder:

    def __init__(self, props):
        self._props = props

    def create_pipeline(self):
        lang = self.props.lang

        return [
            TaskLoggerDecorator(TrainingDataGenerator(lang)),
            TaskLoggerDecorator(Evaluator(lang)),
            TaskLoggerDecorator(ModelTrainer(lang))
        ]
