import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TaskTimerDecorator:

    def __init__(self, task):
        self.task = task

    def execute(self):
        start = datetime.now()
        self.task.execute()
        end = datetime.now() - start
        logging.info(f'Execution time: {end}')
