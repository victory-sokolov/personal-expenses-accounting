import logging
from datetime import datetime


class TaskTimerDecorator:

    def __init__(self, task):
        self.task = task

    def timer(self):
        start = datetime.now()
        self.task.run_tasks()
        elapsed_time = datetime.now() - start
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s'
                            )
        logging.info('Elapsed time: %s', elapsed_time)
