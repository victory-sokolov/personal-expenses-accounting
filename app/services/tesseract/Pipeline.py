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
        tasks = self.pipeline_tasks
        if evaluate == "False":
            tasks = [task[0] for task in tasks if "Evaluator" not in str(task[0])]
        for task in tasks:
            methods = task.__ordered__
            for method in methods:
                func = getattr(task, method)
                if inspect.ismethod(func):
                    func()


@click.command()
@click.option('--evaluate', default=True, help='Evaluate model before and after training.')
def main(evaluate):
    langs = ['lav', 'eng']
    PIPELINE_LIST = []
    for lang in langs:
        PIPELINE_LIST.append(PipelineBuilder(
            ModelProperties(lang)).create_pipeline()
        )
    if not PIPELINE_LIST:
        print("No supported fonts found")
        return

    Pipeline(PIPELINE_LIST).run_tasks(evaluate)


if __name__ == "__main__":
    main()
