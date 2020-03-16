import inspect
import os
from multiprocessing import Process, current_process
from typing import List

import click

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.PipelineBuilder import PipelineBuilder
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator
from app.services.tesseract.utils.ClassMetrics import ClassMetrics
from app.services.tesseract.utils.TaskTimerDecorator import timing


class Pipeline():

    def __init__(self, pipeline_tasks: List):
        self.pipeline_tasks = pipeline_tasks

    @timing
    def run_tasks(self, evaluate) -> None:
        tasks = self.pipeline_tasks[0]
        if evaluate == "False":
            tasks = [task for task in tasks if "Evaluator" not in str(task)]

        for task in tasks:
            methods = task.__ordered__
            for method in methods:
                func = getattr(task, method)
                if inspect.ismethod(func):
                    func()


@click.command()
@click.option('--evaluate', default=True, help='Evaluate model before and after training.')
def main(evaluate):
    PIPELINE_LIST = [
        # PipelineBuilder(ModelProperties('lav')).create_pipeline(),
        PipelineBuilder(ModelProperties('eng', 50, 10)).create_pipeline()
    ]
    Pipeline(PIPELINE_LIST).run_tasks(evaluate)


if __name__ == "__main__":
    main()
