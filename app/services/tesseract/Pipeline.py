import inspect
from typing import List
from multiprocessing import Process, current_process
import os
from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.PipelineBuilder import PipelineBuilder
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator
from app.utils.ClassMetrics import ClassMetrics
from app.utils.TaskTimerDecorator import TaskTimerDecorator


class Pipeline():

    def __init__(self, pipeline_tasks: List):
        self.pipeline_tasks = pipeline_tasks

    def run_tasks(self) -> None:
        for task in self.pipeline_tasks:
            for current_task in task:
                methods = current_task.__ordered__
                for method in methods:
                    func = getattr(current_task, method)
                    if inspect.ismethod(func):
                        func()


PIPELINE_LIST = [
    PipelineBuilder(ModelProperties('lav', 50, 5)).create_pipeline(),
    PipelineBuilder(ModelProperties('eng', 50, 5)).create_pipeline()
]

TaskTimerDecorator(Pipeline(PIPELINE_LIST)).timer()

# for proc in PIPELINE_LIST:

#     process = Process(target=TaskTimerDecorator(
#         Pipeline(PIPELINE_LIST)).timer()
#     )
#     process.start()
#     process.join()
