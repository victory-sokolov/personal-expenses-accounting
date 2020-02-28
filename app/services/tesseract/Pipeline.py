import concurrent.futures
import inspect
import sys
from typing import List

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.PipelineBuilder import PipelineBuilder
from app.services.tesseract.ProcessManager import ProcessManager
from app.services.tesseract.TrainingDataGenerator import TrainingDataGenerator
from app.utils.ClassMetrics import ClassMetrics


class Pipeline():

    def __init__(self, pipeline_tasks: List):
        self.pipeline_tasks = pipeline_tasks

    def run_tasks(self) -> None:
        for task in self.pipeline_tasks:
            methods = task.__ordered__
            for method in methods:
                func = getattr(task, method)
                if inspect.ismethod(func):
                    func()


MODEL = ModelProperties('eng')
PIPELINE_LIST = PipelineBuilder(MODEL).create_pipeline()
Pipeline(PIPELINE_LIST).run_tasks()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_sometinhg, arg)]
