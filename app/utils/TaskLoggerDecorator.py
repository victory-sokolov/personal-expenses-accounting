import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TaskLoggerDecorator:

    def __init__(self, task):
        self.task = task

    def execute(self):
        start = datetime.now()
        self.task.execute()
        end = datetime.now() - start

    # def exectime(self, func):
    #     def wrapper(*args, **kwargs):
    #         start = datetime.now()
    #         result = func(*args, **kwargs)
    #         end = datetime.now() - start
    #         logging.info(f'Execution time: {end}')
    #         return result
    #     return wrapper
