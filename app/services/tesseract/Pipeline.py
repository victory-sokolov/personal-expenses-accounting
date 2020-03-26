import inspect
import os
from multiprocessing import Process, current_process
from typing import List

import click

from ModelProperties import ModelProperties
from PipelineBuilder import PipelineBuilder
from ProcessManager import ProcessManager
from TrainingDataGenerator import TrainingDataGenerator
from utils.ClassMetrics import ClassMetrics
from utils.TaskTimerDecorator import timing


class Pipeline():

    def __init__(self, pipeline_tasks: List):
        self.pipeline_tasks = pipeline_tasks

    @timing
    def run_tasks(self, evaluate) -> None:
        tasks = [task[0] for task in self.pipeline_tasks]
        if evaluate == "False":
            tasks = [task for task in tasks if "Evaluator" not in str(task)]
        for task in tasks:
            print(task)
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
