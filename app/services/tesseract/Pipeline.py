from typing import List

from app.services.tesseract.ModelProperties import ModelProperties
from app.services.tesseract.PipelineBuilder import PipelineBuilder
from app.utils.ClassMetrics import ClassMetrics


class Pipeline(object):

    def __init__(self, pipeline_tasks: List):
        self.pipeline_tasks = pipeline_tasks

    def methods(self, class_name) -> List:
        methods = ClassMetrics.get_list_of_methods(class_name)
        return [getattr(class_name, method) for method in methods]

    def run_tasks(self) -> None:
        for task in self.pipeline_tasks:
            methods = self.methods(task)
            for execute in methods:
                execute()


model = ModelProperties('eng')
pipeline_list = PipelineBuilder(model).create_pipeline()

pipeline = Pipeline(pipeline_list).run_tasks()
