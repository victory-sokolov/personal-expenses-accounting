import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class TaskTimerDecorator:

    def __init__(self, task):
        self.task = task

    def timer(self):
        start = datetime.now()
        self.task.run_tasks()
        elapsed_time = datetime.now() - start
        logging.info('Elapsed time: {:.4f} '.format(elapsed_time))
