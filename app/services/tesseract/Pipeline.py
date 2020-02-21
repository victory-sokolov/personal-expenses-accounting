from app.services.tesseract import PipelineBuilder

class Pipeline:

  def __init__(self, pipelineTasks: list):
    self.pipeline_tasks = pipelineTasks


  def execute(self):
      for task in self.pipelineTasks:
        task.execute()
